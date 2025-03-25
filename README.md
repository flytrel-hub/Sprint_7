# Sprint_7: Тестирование API Яндекс Самокат

Этот проект содержит автотесты для API учебного сервиса Яндекс Самокат (`https://qa-scooter.praktikum-services.ru/`). Тесты проверяют основные endpoints, такие как создание курьера, авторизация, создание заказа и получение списка заказов.

## Описание
Проект разработан для тестирования API с использованием Python, библиотеки `pytest` и генерации отчётов через Allure. Тесты проверяют корректность работы API, обработку ошибок и соответствие документации (`qa-scooter.praktikum-services.ru/docs/`).

## Инструкцияпо запуску

1. **Клонируйте репозиторий:**
   ```bash
   git clone <URL_репозитория>
   cd Sprint_7

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt

3. **Запуск тестов:**
    ```bash
    pytest --alluredir=./target/allure-results -v

4. **Просмотр Allure-отчёта:**
    ```bash
    allure serve ./target/allure-results