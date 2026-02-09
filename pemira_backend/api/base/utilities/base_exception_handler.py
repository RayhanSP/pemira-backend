import logging
from dataclasses import asdict

from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler

from pemira_backend.api.base.serializers import ExceptionResponse
from pemira_backend.core.base.specs import ExceptionResult
from pemira_backend.core.base.utilities.dictionary_utility import DictionaryUtil
from pemira_backend import settings


class CommonException(Exception):
    def __init__(self, message, status_code=500):
        self.message = message
        self.status_code = status_code

def base_exception_handler(exc, context):
    logging.error(exc)

    exception_result = ExceptionResult(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_message="Internal Server Error",
    )

    if isinstance(exc, CommonException):
        exception_result.error_message = exc.message

    elif isinstance(exc, ValidationError):
        try:
            args = dict(exc.args[0])
            attr = list(args.keys())[0]
            message = args.get(attr)[0].__str__()
            composed_message = f"{attr}: {message}" if attr != "non_field_errors" else message
            exception_result.error_message = composed_message
        except:
            exception_result.error_message = "Please, check again your data!"

    elif isinstance(exc, APIException):
        exception_result.error_message = exc.detail

    elif settings.DEBUG:
            return exception_handler(exc, context)

    exception_result.status_code = exc.status_code

    return Response(
        data=ExceptionResponse(
            DictionaryUtil.transform_into_jsonable_dictionary(asdict(exception_result))
        ).data,
        status=exception_result.status_code
    )
