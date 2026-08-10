from pages.calc_page import CalcPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestCalc:
    @pytest.fixture
    def driver(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_calc(self, driver):
        calc_page = CalcPage(driver)
        calc_page.open_calc(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
            )
        calc_page.delay_field(45)
        calc_page.button_calc()
        result = calc_page.get_result_with_expected("15")

        assert result == "15", f"Ожидалось 15, получено {result}"
