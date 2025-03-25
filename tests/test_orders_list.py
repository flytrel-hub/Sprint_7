import allure


@allure.feature("Order API")
class TestOrdersList:
    @allure.story("Order List")
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self, setup):
        api = setup
        response = api.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
