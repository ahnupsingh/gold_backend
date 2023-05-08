import logging

log = logging.getLogger(__name__)


class APIAccessor:
    @classmethod
    def request(cls, request_api, **args):
        log.debug("API request: {}, for data: {}".format(request_api, args))

        response = request_api(**args)
        log.debug("BSE response: {}".format(response))

        return 1, '', response
