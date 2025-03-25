import requests
import random
import string


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

    def create_courier(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = self.register_courier(payload)
        if response.status_code == 201:
            login_response = self.login_courier({"login": login, "password": password})
            courier_id = login_response.json()["id"] if login_response.status_code == 200 else None
            return [login, password, first_name, courier_id]
        return []
