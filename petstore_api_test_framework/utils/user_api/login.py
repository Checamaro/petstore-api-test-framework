import allure

from petstore_api_test_framework.basemodels.user import user_login
from petstore_api_test_framework.utils import api_requests


def login(api_url, headers, username, password):
    with (allure.step('Проходим авторизацию')):
        method = 'GET'
        endpoint = '/v2/user/login/'
        query_params = f'username={username}&password={password}'

        with allure.step(f'Отправить {method} запрос на {endpoint}?{query_params}'):
            response = api_requests.send_request(method=method, url=f'{api_url}{endpoint}?{query_params}',
                                                 headers=headers)
            user_login_response = response.json()

        with allure.step('Проверяем, что API возвращает 200 код ответа'):
            assert response.status_code == 200, (f'User login into the system error. Response code:'
                                                 f'{response.status_code} Response body: {response.json()}')
        with allure.step('Проверка ответа на авторизацию пользователя'):
            assert user_login_response['message'].startswith('logged in user session:'
                                                             ), f'User login into the system error. ' \
                                                                               f'Response body: {response.json()}'

        with allure.step('Валидация типов данных полученного тела ответа'):
            user_login.UserLoginResponse(
                code=user_login_response['code'],
                type=user_login_response['type'],
                message=user_login_response['message']
            )
