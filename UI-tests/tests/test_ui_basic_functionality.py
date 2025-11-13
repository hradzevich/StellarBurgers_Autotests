import allure
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.header_page import HeaderPage
from helper import random_ingredient


@allure.parent_suite("UI тесты Stellar Burgers ")
@allure.suite("Главная страница")
@allure.sub_suite("Основная функциональность")
class TestMainPageFunctionality:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        header = HeaderPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        # Открываем страницу ленты заказов, так как
        # при загрузке главной раздел "Конструктор" выбран по умолчанию
        orders_feed_page.open_and_wait_orders_feed_page()
        header.click_on_constructor_section()

        assert (
            main_page.is_current_url_main_page()
        ), "URL не соответствует странице главной странице"
        assert (
            main_page.is_selected_section_constructor()
        ), "Раздел 'Конструктор' не выбран"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_orders_feed(self, driver):
        main_page = MainPage(driver)
        header = HeaderPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page.open_and_wait_main_page()
        header.click_on_orders_feed_section()

        assert (
            orders_feed_page.is_current_url_orders_feed_page()
        ), "URL не соответствует странице Ленты заказов"
        assert (
            orders_feed_page.is_selected_section_orders_feed()
        ), "Раздел 'Лента заказов' не выбран"

    @allure.title("Открытие всплывающего окна при клике на ингредиент")
    def test_open_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_and_wait_main_page()
        ingredient = random_ingredient()
        main_page.click_on_ingredient(ingredient)

        assert main_page.is_popup_displayed(), "Всплывающее окно не открылось"
        assert main_page.is_ingredient_name_correct(
            ingredient
        ), "Имя ингредиента не соответствует выбранному"

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_close_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_and_wait_main_page()
        ingredient = random_ingredient()
        main_page.click_on_ingredient(ingredient)
        main_page.click_to_close_popup()

        assert main_page.is_popup_closed(), "Всплывающее окно не закрылось"

    @allure.title("Счётчик ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_and_wait_main_page()
        ingredient = random_ingredient()
        before_counter_value = main_page.get_counter_value_for_ingredient(ingredient)
        main_page.add_ingredient_to_basket(ingredient)
        after_counter_value = main_page.get_counter_value_for_ingredient(ingredient)

        assert (
            after_counter_value == before_counter_value + 1
        ), f"Счетчик не увеличился: было {before_counter_value}, стало {after_counter_value}"
