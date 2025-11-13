# Этот файл содержит локаторы, которые используются
# для взаимодействия с элементами на странице "Лента заказов"  веб-приложения Stellar Burgers

from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:

    TOTAL_ORDERS = (
        By.XPATH,
        ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number') and contains(@class,'text_type_digits-large')]",
    )

    DAILY_ORDERS = (
        By.XPATH,
        ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number') and contains(@class,'text_type_digits-large')]",
    )

    ORDER_IN_WORK_NUMBERS = (
        By.XPATH,
        ".//ul[contains(@class,'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]",
    )

    ALL_ORDERS_READY_MESSAGE = (
        By.XPATH,
        ".//ul[contains(@class,'OrderFeed_orderListReady')]/li[contains(@class,'text_type_main-small') and text()='Все текущие заказы готовы!']",
    )
