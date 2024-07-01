import requests
import allure
from petstore_api_test_framework.utils import attach


def send_request(method, url, **kwargs):
    with allure.step(f"Send API {method} Request to endpoint {method}"):
        response = requests.request(method=method, url=url, **kwargs)

        attach.response_attaching(response)
        attach.logging_response(response)

        return response
