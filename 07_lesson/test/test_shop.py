import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShop:

    @pytest.fixture
    def driver(self):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_shop(self, driver):
        login_page = LoginPage(driver)
        login_page.open("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        main_page = MainPage(driver)
        main_page.add_all_items_to_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("Анна", "Панкова", "400074")
        checkout_page.click_continue()
        total = checkout_page.get_total()
        expected_total = "Total: $58.29"

        assert total == expected_total, (
            f"Ожидалось: {expected_total}, "
            f"Получено: {total}"
        )

        total_price = checkout_page.get_total_price()
        assert total_price == 58.29, (
            f"Ожидалось: 58.29, "
            f"Получено: {total_price}"
        )

        print(f"\n✅ Тест пройден! Итоговая стоимость: {total}")
