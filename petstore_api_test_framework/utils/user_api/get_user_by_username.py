import allure

from petstore_api_test_framework.basemodels.user import user_get_by_username
from petstore_api_test_framework.utils import api_requests


def get_user_by_username(api_url, headers, username):
    with allure.step('Получаем пользователя по username'):
        method = 'GET'
        endpoint = f'/v2/user/{username}'

        with allure.step(f'Отправить {method} запрос на {endpoint} для получения пользователя'):
            response = api_requests.send_request(method=method, url=f'{api_url}{endpoint}', headers=headers)
            get_user_by_username_response_json = response.json()

        with allure.step('Проверяем, что API возвращает 200 код ответа'):
            assert response.status_code == 200, (f'Get user by username error. '
                                                 f'Response code: {response.status_code} '
                                                 f'Response body: {response.json()}')

        with allure.step('Проверка ответа на пользователя по username'):
            assert get_user_by_username_response_json['username'] == username, (f'Get user by username error. '
                                                                                f'Response body: {response.json()}')

        with allure.step('Валидация типов данных полученного тела ответа'):
            user_get_by_username.GetUserByUsernameResponse(
                id=get_user_by_username_response_json['id'],
                username=get_user_by_username_response_json['username'],
                firstName=get_user_by_username_response_json['firstName'],
                lastName=get_user_by_username_response_json['lastName'],
                email=get_user_by_username_response_json['email'],
                password=get_user_by_username_response_json['password'],
                phone=get_user_by_username_response_json['phone'],
                userStatus=get_user_by_username_response_json['userStatus']
            )
