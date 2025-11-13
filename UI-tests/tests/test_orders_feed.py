import pytest
import allure
from pages.orders_feed_page import OrdersFeedPage
from pages.main_page import MainPage
from locators.orders_feed_locators import OrdersFeedPageLocators
from helper import is_order_number_present


@allure.parent_suite("UI тесты Stellar Burgers ")
@allure.suite("Лента заказов")
@allure.sub_suite("Обновление счётчиков и статусов заказов")
class TestOrdersFeed:
    @pytest.mark.parametrize(
        "name_of_counter, locator",
        [
            ["Выполнено за всё время", OrdersFeedPageLocators.TOTAL_ORDERS],
            ["Выполнено за сегодня", OrdersFeedPageLocators.DAILY_ORDERS],
        ],
    )
    def test_orders_counter_increases_after_creating_new_order(
        self,
        authorized_driver,
        name_of_counter,
        locator,
    ):
        allure.dynamic.title(
            f"Счетчик '{name_of_counter}' увеличивается после создания заказа"
        )
        orders_feed_page = OrdersFeedPage(authorized_driver)
        orders_feed_page.open_and_wait_orders_feed_page()
        before_value = orders_feed_page.get_orders_counter_value(locator)

        main_page = MainPage(authorized_driver)
        main_page.open_and_wait_main_page()
        _ = main_page.create_order()

        orders_feed_page.open_and_wait_orders_feed_page()
        after_value = orders_feed_page.get_orders_counter_value(locator)

        with allure.step(f"Проверить, что счетчик {name_of_counter} увеличился"):
            assert (
                after_value == before_value + 1
            ), f"Ожидалось {before_value + 1}, получено {after_value}"

    @allure.title("Номер созданного заказа отображается в разделе 'В работе'")
    def test_order_number_appears_in_progress_section_after_creation(
        self,
        authorized_driver,
    ):
        main_page = MainPage(authorized_driver)
        main_page.open_and_wait_main_page()
        order_number = main_page.create_order()

        orders_feed_page = OrdersFeedPage(authorized_driver)
        orders_feed_page.open_and_wait_orders_feed_page()

        orders_in_progress = orders_feed_page.get_orders_in_progress()

        with allure.step(
            f"Проверить, что номер нового заказа {order_number} появился в разделе 'В работе'"
        ):
            assert is_order_number_present(
                orders_in_progress, order_number
            ), f"Заказ {order_number} не найден в списке 'В работе'"
