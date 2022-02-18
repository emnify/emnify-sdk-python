import requests
from emnify.api_manager import BaseApiManager
from emnify.const import RequestsTypeEnum
from emnify.errors import ValidationErrorException


class GetAllDevicesApiCall(BaseApiManager):
    request_url_prefix = '/v1/endpoint'
    request_method_name = RequestsTypeEnum.GET.value


class GetEventsByDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/event'
    request_method_name = RequestsTypeEnum.GET.value


class CreateDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint'
    request_method_name = RequestsTypeEnum.POST.value
    response_handlers = {
        200: 'return_unwrapped',
        401: 'unauthorised',
        422: 'process_exception'
    }

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException(f'{response.json()}')


class GetAllSmsFromDevice(BaseApiManager):
    request_url_prefix = '/api/v1/endpoint/{endpoint_id}/sms'
    request_method_name = RequestsTypeEnum.GET.value


class SendSmsToDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/sms'
    request_method_name = RequestsTypeEnum.POST.value
    response_handlers = {
        201: 'return_success',
        401: 'unauthorised',
    }


class RetrieveDevice(BaseApiManager):
    request_url_prefix = '/api/v1/endpoint/{endpoint_id}'
    request_method_name = RequestsTypeEnum.GET.value


class UpdateDevice(BaseApiManager):
    request_url_prefix = '/api/v1/endpoint/{endpoint_id}'
    request_method_name = RequestsTypeEnum.PATCH.value
    response_handlers = {
        204: 'return_success',
        401: 'unauthorised',
    }
