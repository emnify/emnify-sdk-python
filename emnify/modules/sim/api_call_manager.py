import requests
from emnify.api_manager import BaseApiManager
from emnify.constants import RequestsType
from emnify.errors import ValidationErrorException


class SimListApi(BaseApiManager):
    request_url_prefix = '/v1/sim'
    request_method_name = RequestsType.GET.value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response_handlers = self.response_handlers.copy() | {
            200: 'return_paginator'
        }


class SimActivateApi(BaseApiManager):
    request_url_prefix = '/v1/sim_batch/bic/{bic}'
    request_method_name = RequestsType.PATCH.value

    response_handlers = {
        200: 'return_unwrapped',
        401: 'unauthorised',
        422: 'process_exception'
    }

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException('Invalid bic number')


class SimUpdateApi(BaseApiManager):
    request_url_prefix = '/v1/sim/{sim}'
    request_method_name = RequestsType.PATCH.value

    response_handlers = {
        204: 'return_success',
        401: 'unauthorised',
        400: 'process_exception',
        422: 'unauthorised'
    }

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException(response.json())


class SimRetrieveApi(BaseApiManager):
    request_url_prefix = '/v1/sim/{sim}'
    request_method_name = RequestsType.GET.value
