import time

import logging
import json
from json import JSONDecodeError

from django.conf import settings
from rest_framework.authentication import get_authorization_header

log = logging.getLogger(__name__)


class APIParserMiddleware:
    exception_urls = ['/admin/']

    def __init__(self, get_response):
        self.start_time = None
        self.get_response = get_response

    def __call__(self, request):
        self.start_time = time.time()

        if request.path not in self.exception_urls:
            input_request = ''

            if request.method == 'GET':
                input_request = "[GET] {}".format(json.dumps(request.GET))
            elif request.method == 'POST':
                if request.body:
                    input_request = "[POST] {}".format(json.loads(request.body))
                else:
                    input_request = json.dumps(request.POST)

            request_message = "[PATH] {} [REQUEST] {}".format(request.path, input_request)

            auth = get_authorization_header(request).split()
            if auth and len(auth) == 2 and auth[0].lower() == b'token' and len(auth[1]) >= 4:
                request_message = "[TOKEN] {} {}".format(auth[1][:4], request_message)

            log.info(request_message)

        response = self.get_response(request)

        self.log_response(request, response)
        return response

    def log_response(self, request, response):
        duration = 0
        if self.start_time:
            duration = int((time.time() - self.start_time) * 1000)

        if (hasattr(response, 'content') and not request.path.startswith("/admin/") and not request.path.startswith(
                "/uploads/") and b'html' not in response.content and 'document' not in request.path):
            try:
                json_content = json.loads(response.content)
            except JSONDecodeError as _:
                json_content = 'Json parsing error'

            response_message = "[RESPONSE] [PATH] {} [TIME] {} ms [STATUS_CODE] {} [CONTENT] {}".format(
                request.path, duration, response.status_code, json_content)
            log.info(response_message)

        return response

    def process_exception(self, _, exception):
        log.exception("[EXCEPTION] [500]: " + str(exception))
