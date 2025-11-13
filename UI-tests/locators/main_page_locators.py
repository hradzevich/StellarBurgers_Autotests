# Этот файл содержит локаторы, которые используются
# для взаимодействия с элементами на главной странице  веб-приложения Stellar Burgers

from selenium.webdriver.common.by import By


class MainPageLocators:

    @staticmethod
    def ingredient_by_name(name):
        return (
            By.XPATH,
            f".//p[text()='{name}']/preceding-sibling::img[contains(@class,'BurgerIngredient')]",
        )

    INGREDIENT_POPUP = (
        By.XPATH,
        ".//h2[text()='Детали ингредиента']/parent::div[contains(@class, 'Modal_modal')]",
    )

    INGREDIENT_NAME_POPUP = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal') and contains(@class,'opened')]//p[contains(@class,'text_type_main-medium')]",
    )

    CLOSE_POPUP_BTN = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal') and contains(@class,'opened')]//button[contains(@class,'Modal_modal__close')]",
    )

    BASKET = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")

    @staticmethod
    def ingredient_counter_by_name(name):
        return (
            By.XPATH,
            f".//p[text()='{name}']/preceding-sibling::div[contains(@class,'counter_counter')]/p",
        )

    PLACE_ORDER_BTN = (
        By.XPATH,
        ".//button[text()='Оформить заказ']",
    )

    ORDER_PLACED_POPUP = (
        By.XPATH,
        ".//div[contains(@class, 'Modal_modal__contentBox')]",
    )

    ORDER_NUMBER_IN_POPUP = (
        By.XPATH,
        ".//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]",
    )

    CLOSE_ORDER_PLACED_POPUP_BTN = (
        By.XPATH,
        f".//div[contains(@class, 'Modal_modal__contentBox')]/following-sibling::button[contains(@class, 'Modal_modal__close')]",
    )
