import allure

from petstore_api_test_framework.basemodels.user import user_logout
from petstore_api_test_framework.utils import api_requests


def logout(api_url, headers):
    with allure.step('Выйти из системы'):
        method = 'GET'
        endpoint = '/v2/user/logout/'

        with allure.step(f'Отправить {method} запрос на {endpoint} для выхода из системы'):
            response = api_requests.send_request(method=method, url=f'{api_url}{endpoint}', headers=headers)
            user_logout_response_json = response.json()

        with allure.step('Проверяем, что API возвращает 200 код ответа'):
            assert response.status_code == 200, (f'Update user error. Response code: {response.status_code}'
                                                 f' Response body: {response.json()}')

        with allure.step('Проверка ответа на выход из системы'):
            assert user_logout_response_json['message'] == 'ok', f'User logout from the system error. ' \
                                                               f'Response body: {response.json()}'

        with allure.step('Валидация типов данных полученного тела ответа'):
            user_logout.UserLogOutResponse(
                code=user_logout_response_json['code'],
                type=user_logout_response_json['type'],
                message=user_logout_response_json['message']
            )
