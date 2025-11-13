# Этот файл содержит базовый класс для работы с веб-страницами при помощи Selenium.
# Класс BasePage предоставляет основные функции для взаимодействия с элементами на странице,
# такие как открытие страницы, ожидание видимости или кликабельности элементов
# и другие действия, которые могут быть использованы в тестах для сервиса Stellar Burgers

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url} и дождаться загрузки")
    def open_url(self, url):
        self.driver.get(url)
        self.wait.until(EC.url_contains(url))

    @allure.step("Получить url текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать пока элемент не станет невидимым")
    def wait_for_element_hide(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Подождать видимости элемента")
    def wait_for_element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проскроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_is_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element_is_visible(locator)
        return element.text

    @allure.step("Получить значение атрибута элемента")
    def get_attribute_value(self, locator, attribute):
        element = self.wait_for_element_is_visible(locator)
        return element.get_attribute(attribute)

    @allure.step("Получить список элементов по локатору")
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Проверить виден ли элемент")
    def is_element_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return bool(elements and elements[0].is_displayed())
