import allure
from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedPageLocators
from locators.base_locators import BaseLocators
from urls import *
import time


class OrdersFeedPage(BasePage):

    @allure.step("Открыть страницу с лентой заказов и дождаться загрузки")
    def open_and_wait_orders_feed_page(self):
        self.open_url(UIUrls.ORDERS_FEED)
        self.wait_for_element_hide(BaseLocators.OVERLAY)

    @allure.step("Проверить, что выбран раздел 'Лента заказов' (aria-current='page')")
    def is_selected_section_orders_feed(self):
        return (
            self.get_attribute_value(
                BaseLocators.ORDERS_FEED_HEADER_SECTION, "aria-current"
            )
            == "page"
        )

    @allure.step("Проверить, что текущий url соответствует странице ленты заказов")
    def is_current_url_orders_feed_page(self):
        return self.get_current_url() == UIUrls.ORDERS_FEED

    @allure.step("Получить значение в счетчике заказов")
    def get_orders_counter_value(self, locator):
        return int(self.get_text_on_element(locator))

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_orders_in_progress(self, timeout=15):
        end_time = time.time() + timeout
        orders = []
        if self.is_element_visible(OrdersFeedPageLocators.ALL_ORDERS_READY_MESSAGE):
            allure.step(
                "Отображается надпись 'Все текущие заказы готовы!' — ждем, пока пропадет"
            )
            self.wait_for_element_hide(OrdersFeedPageLocators.ALL_ORDERS_READY_MESSAGE)

        while time.time() < end_time:
            elements = self.get_elements(OrdersFeedPageLocators.ORDER_IN_WORK_NUMBERS)
            orders = [el.text.strip() for el in elements if el.text.strip()]
            if orders:
                break
        return orders
