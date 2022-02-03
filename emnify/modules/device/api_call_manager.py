from emnify.api_manager import BaseApiManager
from emnify.const import RequestsTypeEnum


class GetAllDevicesApiCall(BaseApiManager):
    request_url_prefix = '/v1/endpoint'
    request_method_name = RequestsTypeEnum.GET.value


class GetEventsByDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{endpoint_id}/event'
    request_method_name = RequestsTypeEnum.GET.value


class CreateDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint'
    request_method_name = RequestsTypeEnum.POST.value
