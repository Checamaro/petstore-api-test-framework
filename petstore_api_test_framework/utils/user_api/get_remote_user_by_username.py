import allure

from petstore_api_test_framework.basemodels.user import user_get_by_username
from petstore_api_test_framework.utils import api_requests


def get_remote_user_by_username(api_url, headers, username):
    with allure.step('Получаем удаленного пользователя по username'):
        method = 'GET'
        endpoint = f'/v2/user/{username}/'

        with allure.step(f'Отправить {method} запрос на {endpoint} получения удаленного пользователя по username'):
            response = api_requests.send_request(method=method, url=f'{api_url}{endpoint}', headers=headers)

            get_remote_user_by_username_response_json = response.json()
        with allure.step('Проверяем, что API возвращает 404 код ответа'):
            assert response.status_code == 404, f'Get remote user by username error. Response code:' \
                                                f'{response.status_code} Response body: {response.json()}'

        with allure.step('Проверка ответа на удаленного пользователя по username'):
            assert get_remote_user_by_username_response_json['message'] == 'User not found', f'Remote user not found' \
                                                                                                f'Response body: {response.json()}'

        with allure.step('Валидация типов данных полученного тела ответа'):
            user_get_by_username.GetRemoteUserByUsernameResponse(
                code=get_remote_user_by_username_response_json['code'],
                type=get_remote_user_by_username_response_json['type'],
                message=get_remote_user_by_username_response_json['message']
            )
#
# import allure
# import requests
#
# from pydantic import ValidationError
# from petstore_api_test_framework.basemodels.user import user_get_by_username
#
#
# def get_remote_user_by_username(api_url, headers, username):
#     with allure.step('Получаем удаленного пользователя по username'):
#         method = 'GET'
#         endpoint = f'/v2/user/{username}/'
#         try:
#             with allure.step(f'Отправить {method} запрос на {endpoint} получения удаленного пользователя по username'):
#                 response = requests.request(method=method, url=f'{api_url}{endpoint}', headers=headers)
#                 get_remote_user_by_username_response_json = response.json()
#
#             with allure.step('Проверяем, что API возвращает 404 код ответа'):
#
#                 assert response.status_code == 404, f'Get remote user by username error. Response code:' \
#                                                     f'{response.status_code} Response body: {response.json()}'
#
#             with allure.step('Валидация типов данных полученного тела ответа'):
#                 try:
#                     user_get_by_username.GetRemoteUserByUsernameResponse(
#                         code=get_remote_user_by_username_response_json['code'],
#                         type=get_remote_user_by_username_response_json['type'],
#                         message=get_remote_user_by_username_response_json['message']
#                     )
#
#                 except ValidationError as e:
#                     with allure.step(f'Валидация типов данных не прошла, ошибка: {e}'):
#                         raise Exception(f'Валидация типов данных не прошла, ошибка: {e}')
#
#             return None
#
#         except requests.ConnectionError as e:
#             with allure.step(f'API connection error: {e}'):
#                 raise Exception(f'API connection error: {e}')