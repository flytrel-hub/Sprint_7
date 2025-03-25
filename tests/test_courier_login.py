import allure


@allure.feature("Courier API")
class TestCourierLogin:
    @allure.story("Courier Login")
    @allure.title("Успешный логин курьера")
    def test_login_success(self, setup, register_new_courier):
        api = setup
        courier_data = register_new_courier
        payload = {"login": courier_data[0], "password": courier_data[1]}
        response = api.login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.story("Courier Login")
    @allure.title("Ошибка при логине с неверным паролем")
    def test_login_wrong_password_fails(self, setup, register_new_courier):
        api = setup
        courier_data = register_new_courier
        payload = {"login": courier_data[0], "password": "wrongpass"}
        response = api.login_courier(payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.story("Courier Login")
    @allure.title("Ошибка при логине без обязательного поля")
    def test_login_missing_field_fails(self, setup):
        api = setup
        payload = {"password": "12345"}
        response = api.login_courier(payload)
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.story("Courier Login")
    @allure.title("Ошибка при логине несуществующего курьера")
    def test_login_nonexistent_user_fails(self, setup):
        api = setup
        payload = {"login": "nonexistent", "password": "12345"}
        response = api.login_courier(payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
