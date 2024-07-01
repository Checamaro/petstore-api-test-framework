import allure
import json

from petstore_api_test_framework.basemodels.user import user_update
from petstore_api_test_framework.utils import api_requests


def update(api_url, headers, username):
    with allure.step('Обновляем пользователя'):
        method = 'PUT'
        endpoint = f'/v2/user/{username}/'
        try:
            with allure.step('Собираем полезную нагрузку'):
                update_user_request = user_update.UserUpdateRequest.parse_raw(user_update.input_json).json()
                user_data = json.loads(user_update.input_json)

            with allure.step(f'Отправить {method} запрос на {endpoint} для обновления пользователя'):
                response = api_requests.send_request(method=method, url=f'{api_url}{endpoint}', headers=headers,
                                                     data=update_user_request)
                update_user_response = response.json()

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                assert response.status_code == 200, (f'Update user error. Response code: {response.status_code}'
                                                     f' Response body: {response.json()}')

            with allure.step('Проверка ответа на обновление пользователя'):
                assert update_user_response['message'] == user_data['message'], f'Update user error. ' \
                                                                               f'Response body: {response.json()}'

            with allure.step('Валидация типов данных полученного тела ответа'):
                user_update.UserUpdateResponse(
                    code=update_user_response['code'],
                    type=update_user_response['type'],
                    message=update_user_response['message']
                )

        finally:
            return user_data
