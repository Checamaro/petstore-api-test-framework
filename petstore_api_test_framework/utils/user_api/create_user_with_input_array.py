import allure
import json

from petstore_api_test_framework.basemodels.user import user_create_with_input_array
from petstore_api_test_framework.utils import api_requests


def create_user_with_input_array(api_url, headers):
    with ((allure.step('Создаем пользователя'))):
        method = 'POST'
        endpoint = '/v2/user/createWithArray/'
        try:
            with allure.step('Собираем полезную нагрузку'):
                create_user_with_input_array_request = \
                    user_create_with_input_array.CreateUserWithInputArrayRequest.parse_raw(
                        user_create_with_input_array.input_json).json()
                user_data = json.loads(user_create_with_input_array.input_json)

            with allure.step(f'Отправить {method} запрос на {endpoint} для создания пользователя'):
                response = api_requests.send_request(method=method, url=f'{api_url}{endpoint}', headers=headers,
                                                     data=create_user_with_input_array_request)
                create_user_with_input_array_json = response.json()

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                assert response.status_code == 200, f'User creation with array error.' \
                                                    f'Response code: {response.status_code}' \
                                                    f'Response body: {response.json()}'

            with allure.step('Проверка ответа на создание пользователя'):
                assert create_user_with_input_array_json['message'] == user_data['message'], (f'User creation with '
                                                                                              f'array error.')
                f'Response body: {response.json()}'

            with allure.step('Валидация типов данных полученного тела ответа'):
                user_create_with_input_array.CreateUserWithInputArrayResponse(
                    code=create_user_with_input_array_json['code'],
                    type=create_user_with_input_array_json['type'],
                    message=create_user_with_input_array_json['message']
                )
        finally:
            return user_data
