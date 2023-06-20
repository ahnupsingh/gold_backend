from rest_framework.decorators import api_view, authentication_classes
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication

from app.api import api
from app.api.response_builder import ResponseBuilder
from app.user.user import User
from app.util import util


def validate_account_creation_inputs(phone_number, email, first_name, last_name):
    if not (phone_number and email and first_name and last_name):
        return api.INVALID_INPUT

    return api.STATUS_SUCCESS


@api_view(['POST'])
def create_account(request):
    """
    Sample code on how an API is setup
    """
    data = request.data
    response_builder = ResponseBuilder()

    phone_number = data.get('phone_number')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    status = validate_account_creation_inputs(phone_number, email, first_name, last_name)
    if util.is_status_failed(status):
        return response_builder.get_ok200_fail_response(status)

    status, message, user = User.create(phone_number, email, first_name, last_name)
    if util.is_status_failed(status):
        return response_builder.get_ok200_fail_response(status)

    serialized_user = User(user).get_serialized()
    result = {'user': serialized_user}

    return response_builder.success().accepted_202().result_object(result).get_response()


@api_view(['POST'])
@authentication_classes((JWTStatelessUserAuthentication,))
def update_user(request):
    """
    Sample code on how authentication will work
    """
    response_builder = ResponseBuilder()
    result = {}

    return response_builder.success().accepted_202().result_object(result).get_response()
