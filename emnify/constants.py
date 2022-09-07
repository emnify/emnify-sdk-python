from enum import Enum
from emnify.version import EMNIFY_PACKAGE_VERSION

class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class DeviceSort(ExtendedEnum):
    ID = 'id'
    STATUS = 'status'
    LAST_UPDATED = 'last_updated'
    CREATED = 'created'
    NAME = 'name'
    TAGS = 'tags'
    IP_ADDRESS = 'ip_address'
    IMEI = 'imei'


class IdValues(ExtendedEnum):
    ID = 'id'


class RequestsType(ExtendedEnum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
    PATCH = 'patch'


class AuthenticateRequestsUrl(ExtendedEnum):
    V1_AUTHENTICATE = '/v1/authenticate'


class RequestDefaultHeadersKeys(ExtendedEnum):
    ACCEPT = 'accept'
    AUTHORIZATION = 'authorization'
    XEmnOriginApp = 'x-emn-origin-app'
    XEmnOriginAppVersion = 'x-emn-origin-app-version'


class RequestDefaultHeadersValues(ExtendedEnum):
    APPLICATION_JSON = 'application/json'
    BEARER_TOKEN = 'Bearer {}'
    PYTHONSDK_VERSION = EMNIFY_PACKAGE_VERSION
    PYTHONSDK = 'PythonSDK'


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


class SimStatusesID(ExtendedEnum):
    ISSUED_ID = 0
    ACTIVATED_ID = 1
    SUSPENDED_ID = 2
    DELETED_ID = 3
    FACTORY_TEST_ID = 4


class SimStatusesDict(ExtendedEnum):
    ISSUED_DICT = {
            "id": 0,
            "description": "Issued"
        }
    ACTIVATED_DICT = {
            "id": 1,
            "description": "Activated"
        }
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


class ResponseHeaders(ExtendedEnum):
    COUNT_PER_PAGE = 'X-Count-Per-Page'
    CURRENT_PAGE = 'X-Current-Page'
    TOTAL_PAGES = 'X-Total-Pages'
    TOTAL_COUNT = 'X-Total-Count'


class SimSort(ExtendedEnum):
    id = 'ID'
    issuer_org = 'ISSUER_ORG'
    reseller_org = 'RESELLER_ORG'
    customer_org = 'CUSTOMER_PRG'
    iccid = 'ICCID'
    status = 'STATUS'
    production_date = 'PRODUCTION_DATE'
    endpoint = 'ENDPOINT'
    model = 'MODEL'


class RequestUrls(ExtendedEnum):
    ENDPOINT_IN_URL = '/v1/endpoint/{endpoint_id}'
