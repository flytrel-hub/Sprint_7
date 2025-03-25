import allure
from constants import StatusCodes


@allure.feature("Order API")
class TestOrdersList:
    @allure.story("Order List")
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self, setup):
        api = setup
        response = api.get_orders_list()
        assert response.status_code == StatusCodes.OK, (
            f"Ожидался код {StatusCodes.OK}, получен {response.status_code}"
        )
        assert "orders" in response.json(), "Ожидался ключ 'track' в ответе"
