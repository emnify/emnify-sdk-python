import requests
import settings

from emnify.errors import UnauthorisedException, JsonDecodeException

# file and class name don't match
class BaseApiManager:

    response_handlers = {
        200: 'return_unwrapped',
        403: 'unauthorised'
    }
    request_url_prefix = ''
    request_method_name = ''

    @staticmethod
    def _build_headers(token=''):
        return { # Headers object keys have different casing, can the be unified
        # Are all these headers necessary?
            "accept": 'application/json',
            "Authorization": f"Bearer {token}",
            "accept-encoding": 'gzip, deflate, br',
            "Content-Type": "application/json"}

    def build_method_url(self, url_params):
        if not isinstance(url_params, list):
            url_params = [url_params]
        return self.request_url_prefix.format(*url_params) # What do you think about using named parameters 'prefix/{device_id}/suffix'.format(device_id = '333') ? This will add automatic check

    def unauthorised(self, response):
        raise UnauthorisedException('Invalid Token')

    @staticmethod
    def return_unwrapped(response: requests.Response) -> requests.Response.json:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            raise JsonDecodeException('error while parsing json for')

    def call_api(self, client, data: dict = None, files=None, path_params: list = None):
        url = self.request_url_prefix
        if path_params:
            url = self.build_method_url(path_params)
        response = self.make_request(client, url, data, files)
        assert response.status_code in self.response_handlers.keys()
         # Instead of having both success and failure at the same map you can process only failures and return everything else unwrapped. especially when no matching key found

        return getattr(self, self.response_handlers[response.status_code])(response)

    @staticmethod
    def make_get_request(main_url: str, method_name: str, headers: dict):
        return requests.get(f'{main_url}{method_name}', headers=headers)

    @staticmethod
    def make_post_request(main_url: str, method_name: str, headers: dict, data: dict = None):
        # The line (f'{main_url}{method_name}' is duplicated, does it deserve to be extracted as a method?
        return requests.post(f'{main_url}{method_name}', headers=headers, data=data)

    def make_request(self, client, method_url: str, data=None, files=None):
        if self.request_method_name not in ('put', 'post', 'get'): # for HTTP methods use enum or a constant
            raise ValueError(f'{self.request_method_name}: This method is not allowed')
        headers = self._build_headers(client.token)

        if self.request_method_name == 'get':
            response = self.make_get_request(settings.MAIN_URL, method_url, headers=headers)
            return response
        if self.request_method_name == 'post':
            response = self.make_post_request(settings.MAIN_URL, method_url, headers=headers, data=data)
            return response
