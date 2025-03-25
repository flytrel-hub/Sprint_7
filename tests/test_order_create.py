import pytest
import allure
from data import TestData
from constants import StatusCodes


@allure.feature("Order API")
class TestOrderCreate:
    @allure.story("Order Creation")
    @allure.title("Создание заказа с различными вариантами цветов")
    @pytest.mark.parametrize("color_data", TestData.order_colors)
    def test_create_order_with_colors(self, setup, color_data):
        api = setup
        payload = {**TestData.order_base, **color_data}
        response = api.create_order(payload)
        assert response.status_code == StatusCodes.CREATED_STATUS_CODE, (
            f"Ожидался код {StatusCodes.CREATED_STATUS_CODE}, получен {response.status_code}"
        )
        assert "track" in response.json(), "Ожидался ключ 'track' в ответе"
