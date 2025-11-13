import pytest
import requests
from selenium import webdriver
from tenacity import retry, stop_after_attempt, wait_fixed

from urls import *
from generators import generate_user_data


# Фикстура для запуска браузера
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


# Фикстура, которая создает одного пользователя на весь прогон
@pytest.fixture(scope="session")
def test_user():
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _create_user():
        register_payload = generate_user_data()
        headers = {"Content-Type": "application/json"}
        register_response = requests.post(
            APIUrls.REGISTER, json=register_payload, headers=headers, timeout=30
        )
        register_response.raise_for_status()
        register_json = register_response.json()
        if not register_json.get("success"):
            login_payload = {
                "email": register_payload["email"],
                "password": register_payload["password"],
            }
            login_response = requests.post(
                APIUrls.LOGIN, json=login_payload, timeout=30
            )
            access_token = login_response.json().get("accessToken")
            refresh_token = login_response.json().get("refreshToken")
        else:
            access_token = register_json.get("accessToken")
            refresh_token = register_json.get("refreshToken")
        return access_token, refresh_token

    access_token, refresh_token = _create_user()

    yield access_token, refresh_token

    headers = {"Authorization": access_token}
    requests.delete(APIUrls.DELETE, headers=headers)


# Фикстура, которая авторизует пользователя в браузере
@pytest.fixture(scope="function")
def authorized_driver(driver, test_user):
    access_token, refresh_token = test_user
    driver.get(UIUrls.MAIN)
    driver.execute_script(
        "localStorage.setItem('accessToken', arguments[0]);", access_token
    )
    driver.execute_script(
        "localStorage.setItem('refreshToken', arguments[0]);", refresh_token
    )
    driver.refresh()
    return driver
