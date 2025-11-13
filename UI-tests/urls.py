# Здесь собраны ссылки для UI и API сервиса Stellar Burgers

BASE_URL = "https://stellarburgers.nomoreparties.site/"


# Ссылки на UI-страницы Stellar Burgers
class UIUrls:
    MAIN = BASE_URL

    LOGIN = f"{MAIN}login"

    ORDERS_FEED = f"{MAIN}feed"


# Ссылки на API-эндпоинты Stellar Burgers
class APIUrls:

    BASE = BASE_URL

    LOGIN = f"{BASE}api/auth/login"

    REGISTER = f"{BASE}api/auth/register"

    DELETE = f"{BASE}api/auth/user"

    INGREDIENTS = f"{BASE}api/ingredients"

    ORDER = f"{BASE}api/orders"
    