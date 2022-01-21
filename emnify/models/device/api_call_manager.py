from emnify.apihelper import BaseApiManager


class GetAllDevicesApiCall(BaseApiManager):
    request_url_prefix = '/v1/endpoint'
    request_method_name = 'get'


class GetEventsByDevice(BaseApiManager):
    request_url_prefix = '/v1/endpoint/{}/event'
    # HTTP methods as enum/constant
    request_method_name = 'get'
