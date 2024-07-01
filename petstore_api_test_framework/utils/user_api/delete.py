import allure

from petstore_api_test_framework.basemodels.user import user_delete
from petstore_api_test_framework.utils import api_requests


def delete(api_url, headers, username):
    with allure.step('Удаляем пользователя'):
        method = 'DELETE'
        endpoint = f'/v2/user/{username}/'

        with allure.step(f'Отправить {method} запрос на {endpoint} для удаления пользователя'):
            response = api_requests.send_request(method=method, url=f'{api_url}{endpoint}', headers=headers)
            delete_user_response_json = response.json()

        with allure.step('Проверяем, что API возвращает 200 код ответа'):
            assert response.status_code == 200, f'User delete error. Response code: {response.status_code}' \
                                                f'Response body: {response.json()}'

        with allure.step('Проверка ответа на удаление пользователя'):
            assert delete_user_response_json['message'] == username, f'User delete. Response body: {response.json()}'

        with allure.step('Валидация типов данных полученного тела ответа'):
            user_delete.DeleteUserResponse(
                code=delete_user_response_json['code'],
                type=delete_user_response_json['type'],
                message=delete_user_response_json['message']
            )
