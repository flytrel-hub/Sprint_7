import allure
from constants import ErrorMessages, StatusCodes


@allure.feature("Courier API")
class TestCourierLogin:
    @allure.story("Courier Login")
    @allure.title("Успешный логин курьера")
    def test_login_success(self, setup, register_new_courier):
        api = setup
        courier_data = register_new_courier
        payload = {"login": courier_data[0], "password": courier_data[1]}
        response = api.login_courier(payload)
        assert response.status_code == 200, (
            f"Ожидался код 200, получен {response.status_code}"
        )
        assert "id" in response.json(), "Ожидался ключ 'id' в ответе"

    @allure.story("Courier Login")
    @allure.title("Ошибка при логине с неверным паролем")
    def test_login_wrong_password_fails(self, setup, register_new_courier):
        api = setup
        courier_data = register_new_courier
        payload = {"login": courier_data[0], "password": "wrongpass"}
        response = api.login_courier(payload)
        assert response.status_code == StatusCodes.NOT_FOUND_STATUS_CODE, (
            f"Ожидался код {StatusCodes.NOT_FOUND_STATUS_CODE}, получен {response.status_code}"
        )
        assert response.json()["message"] == ErrorMessages.COURIER_NOT_FOUND_ERROR, (
            "Сообщение об ошибке не соответствует ожидаемому"
        )

    @allure.story("Courier Login")
    @allure.title("Ошибка при логине без обязательного поля")
    def test_login_missing_field_fails(self, setup):
        api = setup
        payload = {"password": "12345"}
        response = api.login_courier(payload)
        assert response.status_code == StatusCodes.BAD_REQUEST_STATUS_CODE, (
            f"Ожидался код {StatusCodes.BAD_REQUEST_STATUS_CODE}, получен {response.status_code}"
        )
        assert response.json()["message"] == ErrorMessages.COURIER_LOGIN_MISSING_FIELDS_ERROR, (
            "Сообщение об ошибке не соответствует ожидаемому"
        )

    @allure.story("Courier Login")
    @allure.title("Ошибка при логине несуществующего курьера")
    def test_login_nonexistent_user_fails(self, setup):
        api = setup
        payload = {"login": "nonexistent", "password": "12345"}
        response = api.login_courier(payload)
        assert response.status_code == StatusCodes.NOT_FOUND_STATUS_CODE, (
            f"Ожидался код {StatusCodes.NOT_FOUND_STATUS_CODE}, получен {response.status_code}"
        )
        assert response.json()["message"] == ErrorMessages.COURIER_NOT_FOUND_ERROR, (
            "Сообщение об ошибке не соответствует ожидаемому"
        )
