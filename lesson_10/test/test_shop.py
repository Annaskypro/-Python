import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import allure


class TestShop:

    @pytest.fixture
    def driver(self):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Полный процесс оформления заказа")
    @allure.description(
        "Тест проверяет полный сценарий покупки"
        "товаров в интернет-магазине:\n\n"
        "Шаги теста:\n"
        "1. Авторизация пользователя на сайте\n"
        "2. Добавление всех товаров в корзину\n"
        "3. Переход в корзину и нажатие кнопки оформления заказа\n"
        "4. Заполнение формы с персональными данными\n"
        "5. Переход к финальному шагу оформления\n"
        "6. Проверка итоговой суммы заказа\n\n"
        "Ожидаемый результат: Итоговая сумма должна быть $58.29"
        )
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Оформление заказа")
    def test_shop(self, driver):
        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(driver)
            login_page.open("https://www.saucedemo.com/")
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление всех товаров в корзину"):
            main_page = MainPage(driver)
            main_page.add_all_items_to_cart()

        with allure.step("Переход к оформлению заказа"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Заполнение персональных данных"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_form("Анна", "Панкова", "400074")

        with allure.step("Переход к финальному шагу"):
            checkout_page.click_continue()

        with allure.step("Проверка итоговой суммы"):
            total = checkout_page.get_total()
            expected_total = "Total: $58.29"
            assert total == expected_total, (
                f"Ожидалось: {expected_total}, Получено: {total}"
            )
            total_price = checkout_page.get_total_price()
            assert total_price == 58.29
