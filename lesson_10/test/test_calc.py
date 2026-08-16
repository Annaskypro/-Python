from pages.calc_page import CalcPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestCalc:

    @pytest.fixture
    def driver(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Тест сложения 7 + 8 на медленном калькуляторе")
    @allure.description(
        "Тест проверяет корректность выполнения "
        "арифметической операции сложения "
        "на странице медленного калькулятора."
        " Устанавливается задержка в 45 секунд, "
        "после чего выполняется вычисление 7 + 8. Ожидаемый результат: 15."
    )
    @allure.feature("Калькулятор")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calc(self, driver):
        calc_page = CalcPage(driver)
        with allure.step("Открыть страницу калькулятора"):
            calc_page.open_calc(
                "https://bonigarcia.dev/selenium-webdriver-java/"
                "slow-calculator.html")

        with allure.step("Установить задержку в 45 секунд"):
            calc_page.delay_field(45)

        with allure.step("Выполнить вычисление 7 + 8"):
            calc_page.button_calc()

        with allure.step("Получить результат (ожидается: 15)"):
            result = calc_page.get_result_with_expected("15")

        with allure.step("Проверить, что результат равен 15"):
            assert result == "15", f"Ожидалось 15, получено {result}"
