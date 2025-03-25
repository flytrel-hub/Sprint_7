import pytest
import allure


@allure.feature("Order API")
class TestOrdersList:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api = api_client

    @allure.story("Order List")
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = self.api.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
