import os
import typing
import requests

from emnify import errors as emnify_errors
from emnify.modules.api.models import AuthenticationResponse
from emnify import constants as emnify_constants

MAIN_URL = os.environ.get('EMINFY_SDK_API_ENDPOINT_URL', 'https://cdn.emnify.net/api')

MAX_PAGES_IN_PAGINATOR = 1000 # with regular page size 1000...2000 gives max 2_000_000 records

class BaseApiManager:
    """
    Base manager for api calls handling
    """

    response_handlers = {
        200: 'return_unwrapped',
        201: 'return_success',
        401: 'unauthorised',
        204: 'return_success',
        409: 'process_exception'
    }

    request_url_prefix = ''
    request_method_name = ''

    @staticmethod
    def _build_headers(token=''):
        return {
            emnify_constants.RequestDefaultHeadersKeys.ACCEPT.value:
                emnify_constants.RequestDefaultHeadersValues.APPLICATION_JSON.value,

            emnify_constants.RequestDefaultHeadersKeys.AUTHORIZATION.value:
                emnify_constants.RequestDefaultHeadersValues.BEARER_TOKEN.value.format(token),

            emnify_constants.RequestDefaultHeadersKeys.XEmnOriginApp.value:
                emnify_constants.RequestDefaultHeadersValues.PYTHONSDK.value,

            emnify_constants.RequestDefaultHeadersKeys.XEmnOriginAppVersion.value:
                emnify_constants.RequestDefaultHeadersValues.PYTHONSDK_VERSION.value,
        }

    def process_exception(self, response: requests.Response, client, data: dict = None, *args, **kwargs):
        raise emnify_errors.ValidationErrorException(f'{response.json()}')

    def return_paginator(
            self, response: requests.Response, client, data, files, query_params, path_params
    ) -> typing.Generator:
        query_params = query_params or {}
        page = query_params.get('page', 1) if query_params else 1
        total_pages = int(response.headers.get(emnify_constants.ResponseHeaders.TOTAL_PAGES.value))
        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            raise emnify_errors.JsonDecodeException('error while parsing json for')

        for item in response_data:
            yield item

        if page < total_pages and page < MAX_PAGES_IN_PAGINATOR:
            query_params['page'] = page + 1

            next_page_response = self.call_api(client, data, files, query_params=query_params, path_params=path_params)

            for item in next_page_response:
                yield item

    def build_method_url(self, url_params):
        return self.request_url_prefix.format(**url_params)

    def unauthorised(self, response: requests.Response, client, data: dict = None, path_params=None, *args, **kwargs):
        """
        method for 1 cycle retry - re authentication
        """
        auth = Authenticate()
        client.token = AuthenticationResponse(
            **auth.call_api(client, {"application_token": client.app_token})
        ).auth_token

        return self.call_api(client, data, path_params=path_params, *args, **kwargs)

    def call_api(self, client, data: dict = None, files=None, path_params: dict = None, query_params: dict = None):
        url = self.request_url_prefix
        if path_params:
            url = self.build_method_url(path_params)
        response = self.make_request(client, url, data, files, query_params=query_params)
        if response.status_code not in self.response_handlers.keys():
            raise emnify_errors.UnknownStatusCodeException(
                "Unknown status code {status_code}".format(status_code=response.status_code)
            )

        return getattr(self, self.response_handlers[response.status_code])\
            (response, client, data=data, files=files, query_params=query_params, path_params=path_params)

    def make_get_request(self, main_url: str, method_name: str, headers: dict, params: str = None):
        return requests.get(self.resource_path(main_url, method_name), headers=headers, params=params)

    def make_post_request(self, main_url: str, method_name: str, headers: dict, params: dict = None, data: dict = None):
        return requests.post(self.resource_path(main_url, method_name), headers=headers, json=data, params=params)

    def make_patch_request(self, main_url: str, method_name: str, headers: dict, params: dict = None, data: dict = None):
        return requests.patch(self.resource_path(main_url, method_name), headers=headers, json=data, params=params)

    def make_delete_request(self, main_url: str, method_name: str, headers: dict, params: dict = None, data: dict = None):
        return requests.delete(self.resource_path(main_url, method_name), headers=headers, json=data, params=params)

    def make_put_request(self, main_url: str, method_name: str, headers: dict, params: dict = None, data: dict = None):
        return requests.put(self.resource_path(main_url, method_name), headers=headers, json=data, params=params)

    def make_request(self, client, method_url: str, data=None, files=None, query_params=None):
        if self.request_method_name not in emnify_constants.RequestsType.list():
            raise ValueError(f'{self.request_method_name}: This method is not allowed')
        headers = self._build_headers(client.token)
        response = None
        if self.request_method_name == emnify_constants.RequestsType.GET.value:
            response = self.make_get_request(
                MAIN_URL, method_url, headers=headers, params=query_params
            )
        elif self.request_method_name == emnify_constants.RequestsType.POST.value:
            response = self.make_post_request(
                MAIN_URL, method_url, headers=headers, params=query_params, data=data
            )
        elif self.request_method_name == emnify_constants.RequestsType.PATCH.value:
            response = self.make_patch_request(
                MAIN_URL, method_url, headers=headers, params=query_params, data=data
            )
        elif self.request_method_name == emnify_constants.RequestsType.DELETE.value:
            response = self.make_delete_request(
                MAIN_URL, method_url, headers=headers, params=query_params, data=data
            )
        elif self.request_method_name == emnify_constants.RequestsType.PUT.value:
            response = self.make_put_request(
                MAIN_URL, method_url, headers=headers, params=query_params, data=data
            )

        return response

    @staticmethod
    def return_success(*_, **__) -> True:
        return True

    @staticmethod
    def return_unwrapped(response: requests.Response, *args, **kwargs) -> requests.Response.json:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            raise emnify_errors.JsonDecodeException('error while parsing json for')

    @staticmethod
    def resource_path(main_url: str, method_name: str):
        return f'{main_url}{method_name}'


class Authenticate(BaseApiManager):
    request_url_prefix = emnify_constants.AuthenticateRequestsUrl.V1_AUTHENTICATE.value
    request_method_name = emnify_constants.RequestsType.POST.value

    response_handlers = {
        200: 'return_unwrapped',
        401: 'unauthorised',
        404: 'unexpected_error'
    }

    def unauthorised(
            self, response: requests.Response, client, data: dict = None, files=None, path_params: list = None, **kwargs
    ):
        raise emnify_errors.UnauthorisedException('Invalid Application Token')

    def unexpected_error(
            self, response: requests.Response, client, data: dict = None, files=None, path_params: list = None
    ):
        raise emnify_errors.UnauthorisedException(f'Unexpected Auth Error {response.json()}')
