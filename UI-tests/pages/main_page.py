import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators
from urls import *
from data import *
import time


class MainPage(BasePage):

    @allure.step("Открыть главную страницу и дождаться загрузки")
    def open_and_wait_main_page(self):
        self.open_url(UIUrls.MAIN)
        self.wait_for_element_hide(BaseLocators.OVERLAY)

    @allure.step("Проверить, что текущий url соответствует главной странице")
    def is_current_url_main_page(self):
        return self.get_current_url() == UIUrls.MAIN

    @allure.step("Проверить, что выбран раздел 'Конструктор' (aria-current='page')")
    def is_selected_section_constructor(self):
        return (
            self.get_attribute_value(
                BaseLocators.CONSTRUCTOR_HEADER_SECTION, "aria-current"
            )
            == "page"
        )

    @allure.step("Кликнуть на ингредиент '{name}'")
    def click_on_ingredient(self, name):
        self.scroll_to_element(MainPageLocators.ingredient_by_name(name))
        self.click_element(MainPageLocators.ingredient_by_name(name))

    @allure.step("Дождаться появления всплывающего окна 'Детали ингредиента'")
    def is_popup_displayed(self):
        return self.wait_for_element_is_visible(MainPageLocators.INGREDIENT_POPUP)

    @allure.step("Проверить, что название ингредиента в попапе соответствует '{name}'")
    def is_ingredient_name_correct(self, name):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_NAME_POPUP) == name

    @allure.step("Кликнуть крестик всплывающего окна 'Детали ингредиента'")
    def click_to_close_popup(self):
        self.click_element(MainPageLocators.CLOSE_POPUP_BTN)

    @allure.step(
        "Проверить, что всплывающее окно 'Детали ингредиента' не отображается после закрытия"
    )
    def is_popup_closed(self):
        return self.wait_for_element_hide(MainPageLocators.INGREDIENT_POPUP)

    @allure.step("Добавить игредиент {name} в заказ")
    def add_ingredient_to_basket(self, name):
        ingredient = self.wait_for_element_is_visible(
            MainPageLocators.ingredient_by_name(name)
        )
        self.scroll_to_element(MainPageLocators.ingredient_by_name(name))
        target = self.wait_for_element_is_visible(MainPageLocators.BASKET)
        self.drag_and_drop_element(ingredient, target)

    @allure.step("Получить значение в счетчике ингредиента {name}")
    def get_counter_value_for_ingredient(self, name):
        counter_value = int(
            self.get_text_on_element(MainPageLocators.ingredient_counter_by_name(name))
        )
        # Булки добавляются парой (верх+низ), поэтому делим значение на 2
        if "булка" in name.lower():
            counter_value //= 2
        return counter_value

    @allure.step("Оформить заказ")
    def create_order(self):
        ingredients = Ingredients.INGREDIENTS
        for ingr in ingredients:
            self.add_ingredient_to_basket(ingr)
        self.click_element(MainPageLocators.PLACE_ORDER_BTN)
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.wait_for_element_is_visible(MainPageLocators.ORDER_PLACED_POPUP)
        order_number = self.wait_for_real_order_number()
        self.close_order_popup()
        return order_number

    @allure.step("Дождаться появления корректного номера заказа")
    def wait_for_real_order_number(self, timeout=15):
        end_time = time.time() + timeout
        while time.time() < end_time:
            order_number = self.get_text_on_element(
                MainPageLocators.ORDER_NUMBER_IN_POPUP
            )
            if order_number != "9999" and order_number != "":
                return order_number

    @allure.step("Закрыть всплывающее окно с номером заказа")
    def close_order_popup(self):
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_element(MainPageLocators.CLOSE_ORDER_PLACED_POPUP_BTN)
        self.wait_for_element_hide(MainPageLocators.ORDER_PLACED_POPUP)
