from emnify.api_manager import BaseApiManager
from emnify.constants import RequestsType


class GetOperatorList(BaseApiManager):
    request_url_prefix = '/v1/operator'
    request_method_name = RequestsType.GET.value
