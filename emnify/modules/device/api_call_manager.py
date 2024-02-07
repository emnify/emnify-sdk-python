import requests
from emnify.api_manager import BaseApiManager
from emnify.constants import RequestsType, RequestUrls
from emnify.errors import ValidationErrorException


class GetAllDevicesApiCall(BaseApiManager):
    request_url_prefix = '/v1/endpoint'
    request_method_name = RequestsType.GET.value
    response_handlers = {
        200: 'return_paginator',
        401: 'unauthorised',
    }


class GetEventsByDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/event'
    request_method_name = RequestsType.GET.value
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response_handlers = self.response_handlers.copy() | {
            200: 'return_paginator'
        }


class CreateDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint'
    request_method_name = RequestsType.POST.value
    response_handlers = {
        200: 'return_unwrapped',
        201: 'return_success',
        401: 'unauthorised',
        422: 'process_exception'
    }

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException(f'{response.json()}')

    def return_success(self, response: requests.Response, client, data: dict = None, *args, **kwargs) -> True:
        return int(response.headers.get('Location').split('/')[-1])


class GetAllSmsFromDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/sms'
    request_method_name = RequestsType.GET.value


class SendSmsToDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/sms'
    request_method_name = RequestsType.POST.value
    response_handlers = {
        201: 'return_success',
        401: 'unauthorised',
    }


class RetrieveDevice(BaseApiManager):
    request_url_prefix = RequestUrls.ENDPOINT_IN_URL.value
    request_method_name = RequestsType.GET.value


class UpdateDevice(BaseApiManager):
    request_url_prefix = RequestUrls.ENDPOINT_IN_URL.value
    request_method_name = RequestsType.PATCH.value
    response_handlers = {
        204: 'return_success',
        401: 'unauthorised',
    }


class DeleteDevice(BaseApiManager):
    request_url_prefix = RequestUrls.ENDPOINT_IN_URL.value
    request_method_name = RequestsType.DELETE.value


class GetOperatorBlacklist(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/operator_blacklist'
    request_method_name = RequestsType.GET.value


class AddOperatorBlacklist(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/operator_blacklist/{operator_id}'
    request_method_name = RequestsType.PUT.value

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException(
            response.json().get('message', 'This operator is already in blacklist')
        )


class DeleteOperatorBlacklist(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/operator_blacklist/{operator_id}'
    request_method_name = RequestsType.DELETE.value

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException(
            response.json().get('message', 'This operator is not in blacklist')
        )


class ResetConnectivityPatch(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/connectivity'
    request_method_name = RequestsType.PATCH.value


class GetDeviceConnectivity(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/connectivity'
    request_method_name = RequestsType.GET.value

    response_handlers = {
        200: 'return_unwrapped',
        401: 'unauthorised',
        422: 'process_exception',
    }

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException(
            'device_id is not valid'
        )
