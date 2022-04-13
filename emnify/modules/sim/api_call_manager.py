import requests
from emnify.api_manager import BaseApiManager
from emnify.constants import RequestsTypeEnum
from emnify.errors import ValidationErrorException


class SimListApi(BaseApiManager):
    request_url_prefix = '/v1/sim'
    request_method_name = RequestsTypeEnum.GET.value


class SimActivateApi(BaseApiManager):
    request_url_prefix = '/v1/sim_batch/bic/{bic}'
    request_method_name = RequestsTypeEnum.PATCH.value

    response_handlers = {
        200: 'return_unwrapped',
        401: 'unauthorised',
        422: 'process_exception'
    }

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise ValidationErrorException('Invalid bic number')
