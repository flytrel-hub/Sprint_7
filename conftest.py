import pytest
from api_methods import ApiMethods


@pytest.fixture
def api_client():
    return ApiMethods()


@pytest.fixture
def register_new_courier(api_client):
    def _register():
        import random
        import string

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

        response = api_client.register_courier(payload)
        if response.status_code == 201:
            login_response = api_client.login_courier({"login": login, "password": password})
            courier_id = login_response.json()["id"] if login_response.status_code == 200 else None
            return [login, password, first_name, courier_id]
        return []

    return _register
