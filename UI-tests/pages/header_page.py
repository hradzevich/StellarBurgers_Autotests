import allure
from pages.base_page import BasePage
from locators.base_locators import BaseLocators

class HeaderPage(BasePage):

    @allure.step("Кликнуть на заголовок раздела 'Конструктор'")
    def click_on_constructor_section(self):
        self.click_element(BaseLocators.CONSTRUCTOR_HEADER_SECTION)
    
    @allure.step("Кликнуть на заголовок раздела 'Лента заказов")
    def click_on_orders_feed_section(self):
        self.click_element(BaseLocators.ORDERS_FEED_HEADER_SECTION)
