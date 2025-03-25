import pytest
import allure
from data import TestData


@allure.feature("Order API")
class TestOrderCreate:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api = api_client

    @allure.story("Order Creation")
    @allure.title("Создание заказа с различными вариантами цветов")
    @pytest.mark.parametrize("color_data", TestData.order_colors)
    def test_create_order_with_colors(self, color_data):
        payload = {**TestData.order_base, **color_data}
        response = self.api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()