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

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException('Invalid bic number')


class SimUpdateApi(BaseApiManager):
    request_url_prefix = '/v1/sim/{sim}'
    request_method_name = RequestsType.PATCH.value


class SimRetrieveApi(BaseApiManager):
    request_url_prefix = '/v1/sim/{sim}'
    request_method_name = RequestsType.GET.value
