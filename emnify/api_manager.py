import requests
import settings

from emnify.errors import UnauthorisedException, JsonDecodeException
from emnify.modules.api.models import AuthenticationResponse
from emnify.const import RequestsTypeEnum, RequestsUrlEnum, RequestDefaultHeadersKeys, RequestDefaultHeadersValues


class BaseApiManager:

    response_handlers = {
        200: 'return_unwrapped',
        201: 'return_success',
        401: 'unauthorised'
    }
    request_url_prefix = ''
    request_method_name = ''

    @staticmethod
    def _build_headers(token=''):
        return {
            RequestDefaultHeadersKeys.ACCEPT.value: RequestDefaultHeadersValues.APPLICATION_JSON.value,
            RequestDefaultHeadersKeys.AUTHORIZATION.value: RequestDefaultHeadersValues.BEARER_TOKEN.value.format(token)
        }

    def build_method_url(self, url_params):
        return self.request_url_prefix.format(**url_params)

    def unauthorised(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        """
        method for 1 cycle retry - re authentication
        """
        auth = Authenticate()
        client.token = AuthenticationResponse(
            **auth.call_api(client, {"application_token": client.app_token})
        ).auth_token

        return self.call_api(client, data, *args, **kwargs)

    @staticmethod
    def return_success(*_, **__) -> True:
        return True

    @staticmethod
    def return_unwrapped(response: requests.Response, *args, **kwargs) -> requests.Response.json:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            raise JsonDecodeException('error while parsing json for')

    def call_api(self, client, data: dict = None, files=None, path_params: dict = None, query_params: dict = None):
        url = self.request_url_prefix
        if path_params:
            url = self.build_method_url(path_params)
        response = self.make_request(client, url, data, files, query_params=query_params)
        assert response.status_code in self.response_handlers.keys()
        return getattr(self, self.response_handlers[response.status_code])\
            (response, client, data=data, files=files, query_params=query_params)

    @staticmethod
    def make_get_request(main_url: str, method_name: str, headers: dict, params: str = None):
        return requests.get(f'{main_url}{method_name}', headers=headers, params=params)

    @staticmethod
    def make_post_request(main_url: str, method_name: str, headers: dict, data: dict = None):
        return requests.post(f'{main_url}{method_name}', headers=headers, json=data)

    def make_request(self, client, method_url: str, data=None, files=None, query_params=None):
        if self.request_method_name not in RequestsTypeEnum.list():
            raise ValueError(f'{self.request_method_name}: This method is not allowed')
        headers = self._build_headers(client.token)

        if self.request_method_name == RequestsTypeEnum.GET.value:
            response = self.make_get_request(settings.MAIN_URL, method_url, headers=headers, params=query_params)
            return response
        if self.request_method_name == RequestsTypeEnum.POST.value:
            response = self.make_post_request(settings.MAIN_URL, method_url, headers=headers, data=data)
            return response


class Authenticate(BaseApiManager):
    request_url_prefix = RequestsUrlEnum.V1_AUTHENTICATE.value
    request_method_name = RequestsTypeEnum.POST.value

    response_handlers = {
        200: 'return_unwrapped',
        401: 'unauthorised',
        404: 'unexpected_error'
    }

    def unauthorised(
            self, response: requests.Response, client, data: dict = None, files=None, path_params: list = None
    ):
        raise UnauthorisedException('Invalid Application Token')

    def unexpected_error(
            self, response: requests.Response, client, data: dict = None, files=None, path_params: list = None
    ):
        raise UnauthorisedException(f'Unexpected Auth Error {response.json()}')
