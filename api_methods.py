import requests


class ApiMethods:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    def register_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/courier", json=payload)

    def login_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/courier/login", json=payload)

    def create_order(self, payload):
        return requests.post(f"{self.BASE_URL}/orders", json=payload)

    def get_orders_list(self):
        return requests.get(f"{self.BASE_URL}/orders")

    def delete_courier(self, courier_id):
        return requests.delete(f"{self.BASE_URL}/courier/{courier_id}")
