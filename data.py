class TestData:
    courier_valid = {
        "login": "testcourier2",
        "password": "12345",
        "firstName": "JohnSina"
    }

    order_colors = [
        {"color": ["BLACK"]},
        {"color": ["GREY"]},
        {"color": ["BLACK", "GREY"]},
        {"color": []}
    ]

    order_base = {
        "firstName": "Test",
        "lastName": "User",
        "address": "Test street 1",
        "metroStation": 4,
        "phone": "+79991234567",
        "rentTime": 1,
        "deliveryDate": "2025-03-26",
        "comment": "Test order"
    }
