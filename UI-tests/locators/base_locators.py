# Этот файл содержит локаторы элементов, общие для всех страниц приложения Stellar Burgers

from selenium.webdriver.common.by import By


class BaseLocators:

    OVERLAY = (
        By.XPATH,
        ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div",
    )

    CONSTRUCTOR_HEADER_SECTION = (
        By.XPATH,
        ".//p[text()='Конструктор']/parent::a[contains(@class, 'AppHeader_header')]",
    )


    ORDERS_FEED_HEADER_SECTION = (
        By.XPATH,
        ".//p[text()='Лента Заказов']/parent::a[contains(@class, 'AppHeader_header')]",
    )