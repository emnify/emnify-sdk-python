from enum import Enum

from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class DeviceSortEnum(ExtendedEnum):
    ID = 'id'
    STATUS = 'status'
    LAST_UPDATED = 'last_updated'
    CREATED = 'created'
    NAME = 'name'
    TAGS = 'tags'
    IP_ADDRESS = 'ip_address'
    IMEI = 'imei'


class RequestsTypeEnum(ExtendedEnum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'


class RequestsUrlEnum(ExtendedEnum):
    V1_AUTHENTICATE = '/v1/authenticate'


class RequestDefaultHeadersKeys(ExtendedEnum):
    ACCEPT = 'accept'
    AUTHORIZATION = 'authorization'


class RequestDefaultHeadersValues(ExtendedEnum):
    APPLICATION_JSON = 'application/json'
    BEARER_TOKEN = 'Bearer {}'
