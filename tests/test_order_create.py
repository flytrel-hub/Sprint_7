import pytest
import allure
from data import TestData


@allure.feature("Order API")
class TestOrderCreate:
    @allure.story("Order Creation")
    @allure.title("Создание заказа с различными вариантами цветов")
    @pytest.mark.parametrize("color_data", TestData.order_colors)
    def test_create_order_with_colors(self, setup, color_data):
        api = setup
        payload = {**TestData.order_base, **color_data}
        response = api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()
