import pytest
import allure


@allure.feature("Courier API")
class TestCourierCreate:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api = api_client

    @allure.story("Courier Registration")
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, register_new_courier):
        courier_data = register_new_courier()
        assert len(courier_data) == 4
        assert courier_data[3] is not None

    @allure.story("Courier Registration")
    @allure.title("Ошибка при создании курьера с существующим логином")
    def test_create_duplicate_courier_fails(self, register_new_courier):
        courier_data = register_new_courier()
        payload = {"login": courier_data[0], "password": "newpass", "firstName": "New"}
        response = self.api.register_courier(payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.story("Courier Registration")
    @allure.title("Ошибка при создании курьера без обязательного поля")
    def test_create_courier_missing_field_fails(self):
        payload = {"login": "testusercuri"}
        response = self.api.register_courier(payload)
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.story("Courier Registration")
    @allure.title("Проверка успешного ответа при создании курьера")
    def test_create_courier_success_response(self, register_new_courier):
        courier_data = register_new_courier()
        assert len(courier_data) == 4
        new_payload = {
            "login": f"{courier_data[0]}new",
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        response = self.api.register_courier(new_payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}