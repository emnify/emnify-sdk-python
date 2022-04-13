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


class Values(ExtendedEnum):
    ID = 'id'

class RequestsTypeEnum(ExtendedEnum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
    PATCH = 'patch'


class RequestsUrlEnum(ExtendedEnum):
    V1_AUTHENTICATE = '/v1/authenticate'


class RequestDefaultHeadersKeys(ExtendedEnum):
    ACCEPT = 'accept'
    AUTHORIZATION = 'authorization'


class RequestDefaultHeadersValues(ExtendedEnum):
    APPLICATION_JSON = 'application/json'
    BEARER_TOKEN = 'Bearer {}'


class DeviceStatuses(ExtendedEnum):
    ENABLED_ID = 0
    DISABLED_ID = 1
    DELETED_ID = 2
    ENABLED_DICT = {
            "id": 0,
            "description": "Enabled"
        }
    DISABLED_DICT = {
            "id": 1,
            "description": "Disabled"
        }
    DELETED_DICT = {
            "id": 2,
            "description": "Deleted"
        }


class SimStatuses(ExtendedEnum):
    ISSUED_ID = 0
    ACTIVATED_ID = 1
    SUSPENDED_ID = 2
    DELETED_ID = 3
    FACTORY_TEST_ID = 4
    ISSUED_DICT = {
            "id": 0,
            "description": "Issued"
        }
    ACTIVATED_DICT = {
            "id": 1,
            "description": "Activated"
        },
    SUSPENDED_DICT = {
            "id": 2,
            "description": "Suspended"
        }
    DELETED_DICT = {
            "id": 3,
            "description": "Deleted"
        }
    FACTORY_TEST_DICT = {
            "id": 4,
            "description": "Factory Test"
        }


class Example(ExtendedEnum):
    ACTIVATION_CODE = 'AT+CGDCONT=1,"IP","em",,'
    SENDER = "city_scooters_admin"