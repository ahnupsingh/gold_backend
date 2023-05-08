from builtins import object
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

from app.api import api


class ResponseBuilder(object):
    """
    API response builder
    """

    def __init__(self):
        self.results = {}
        self.status_code = 1
        self.status_message = ""
        self.status = status.HTTP_200_OK

    def fail(self):
        self.status_code = -1
        return self

    def message(self, status_message):
        self.status_message = status_message
        return self

    def success(self):
        self.status_code = 1
        return self

    def set_status_code(self, status_code):
        self.status_code = status_code
        return self

    def ok_200(self):
        self.status = status.HTTP_200_OK
        return self

    def accepted_202(self):
        self.status = status.HTTP_202_ACCEPTED
        return self

    def not_found_404(self):
        self.status = status.HTTP_404_NOT_FOUND
        return self

    def bad_request_400(self):
        self.status = status.HTTP_400_BAD_REQUEST
        return self

    def user_unauthorized_401(self):
        self.status = status.HTTP_401_UNAUTHORIZED
        self.status_message = "User Unauthorized"
        return self

    def user_forbidden_403(self):
        self.status = status.HTTP_403_FORBIDDEN
        return self

    def result_object(self, result):
        self.results = result
        return self

    def get_404_not_found_response(self, message):
        self.not_found_404()
        self.message(message)
        self.success()
        return self.get_response()

    def get_response(self):
        content = self.get_json()
        return Response(content, status=self.status)

    def get_json(self):
        status_message = self.status_message
        if self.status_code != 1:
            status_message = api.error_messages[self.status_code]

        return {
            'status-code': self.status_code,
            'status-message': status_message,
            'data': self.results,
        }

    def get_json_response(self):
        content = self.get_json()
        return JsonResponse(content)

    @staticmethod
    def return_failed_json_response(message):
        return ResponseBuilder().ok_200().fail().message(message).get_json_response()

    def get_ok200_fail_response(self, error_code):
        return self.ok_200().fail().set_status_code(error_code).get_response()
