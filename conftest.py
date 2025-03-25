import pytest
from api_methods import ApiMethods


@pytest.fixture
def api_client():
    return ApiMethods()


@pytest.fixture
def register_new_courier(api_client):
    courier_data = api_client.create_courier()

    yield courier_data

    courier_id = courier_data[3] if len(courier_data) > 0 else None
    if courier_id:
        api_client.delete_courier(courier_id)


@pytest.fixture(autouse=True)
def setup(api_client):
    return api_client
