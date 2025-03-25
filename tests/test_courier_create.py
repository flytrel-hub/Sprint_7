import allure
from constants import ErrorMessages, StatusCodes, ApiResponses


@allure.feature("Courier API")
class TestCourierCreate:
    @allure.story("Courier Registration")
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, register_new_courier):
        courier_data = register_new_courier
        assert len(courier_data) == 4
        assert courier_data[3] is not None

    @allure.story("Courier Registration")
    @allure.title("Ошибка при создании курьера с существующим логином")
    def test_create_duplicate_courier_fails(self, setup, register_new_courier):
        api = setup
        courier_data = register_new_courier
        payload = {"login": courier_data[0], "password": "newpass", "firstName": "New"}
        response = api.register_courier(payload)
        assert response.status_code == StatusCodes.CONFLICT_STATUS_CODE, (
            f"Ожидался код {StatusCodes.CONFLICT_STATUS_CODE}, получен {response.status_code}"
        )
        assert response.json()["message"] == ErrorMessages.COURIER_DUPLICATE_LOGIN_ERROR, (
            "Сообщение об ошибке не соответствует ожидаемому"
        )

    @allure.story("Courier Registration")
    @allure.title("Ошибка при создании курьера без обязательного поля")
    def test_create_courier_missing_field_fails(self, setup):
        api = setup
        payload = {"login": "testusercuri"}
        response = api.register_courier(payload)
        assert response.status_code == StatusCodes.BAD_REQUEST_STATUS_CODE, (
            f"Ожидался код {StatusCodes.BAD_REQUEST_STATUS_CODE}, получен {response.status_code}"
        )
        assert response.json()["message"] == ErrorMessages.COURIER_MISSING_FIELDS_ERROR, (
            "Сообщение об ошибке не соответствует ожидаемому"
        )

    @allure.story("Courier Registration")
    @allure.title("Проверка успешного ответа при создании курьера")
    def test_create_courier_success_response(self, setup, register_new_courier):
        api = setup
        courier_data = register_new_courier
        assert len(courier_data) == 4
        new_payload = {
            "login": f"{courier_data[0]}new",
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        response = api.register_courier(new_payload)
        assert response.status_code == StatusCodes.CREATED_STATUS_CODE, (
            f"Ожидался код {StatusCodes.CREATED_STATUS_CODE}, получен {response.status_code}"
        )
        assert response.json() == ApiResponses.SUCCESS_RESPONSE, (
            "Ответ API не соответствует ожидаемому"
        )
