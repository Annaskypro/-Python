from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    """
    Класс для работы со страницей калькулятора.

    Этот класс предоставляет методы для взаимодействия
      с элементами калькулятора,
    включая установку задержки, нажатие кнопок и получение результата.

        Attributes:
        driver (selenium.webdriver.remote.webdriver.WebDriver):
          Веб-драйвер Selenium.
        wait (selenium.webdriver.support.ui.WebDriverWait):
          Объект для явного ожидания.
        DELAY (tuple): Локатор поля ввода задержки.
        BUTTON_7 (tuple): Локатор кнопки "7".
        BUTTON_plus (tuple): Локатор кнопки "+".
        BUTTON_8 (tuple): Локатор кнопки "8".
        BUTTON_equals (tuple): Локатор кнопки "=".
        RESULT (tuple): Локатор поля c результатом.
    """

    DELAY = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_plus = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_equals = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        """
        Конструктор класса CalcPage.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    @allure.step("Открыть страницу калькулятора по URL: {url}")
    def open_calc(self, url: str) -> None:
        """
        Открывает страницу калькулятора по указанному URL.
        """
        self.driver.get(url)

    @allure.step("Установить задержку в поле ввода: {time_delay} секунд")
    def delay_field(self, time_delay: int) -> None:
        """
        Устанавливает значение задержки в поле ввода.
        """
        delay_input = self.driver.find_element(*self.DELAY)
        delay_input.clear()
        delay_input.send_keys(str(time_delay))

    @allure.step("Выполнить последовательность нажатий"
                 "на кнопки калькулятора: 7 -> + -> 8 -> =")
    def button_calc(self) -> None:
        """
        Выполняет последовательность нажатий на кнопки калькулятора:
        7 -> + -> 8 -> =
        Использует явное ожидание для каждого элемента.
        """
        with allure.step("Нажать кнопку '7'"):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_7)).click()

        with allure.step("Нажать кнопку '+'"):
            self.wait.until(EC.element_to_be_clickable(
                self.BUTTON_plus)).click()

        with allure.step("Нажать кнопку '8'"):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_8)).click()

        with allure.step("Нажать кнопку '='"):
            self.wait.until(EC.element_to_be_clickable(
                self.BUTTON_equals)).click()

    @allure.step("Ожидать появления результата "
                 "'{expected_value}' и получить его")
    def get_result_with_expected(self, expected_value: str) -> str:
        """
        Ожидает появления ожидаемого значения в поле
            результата и возвращает его.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT, expected_value)
        )
        return self.driver.find_element(*self.RESULT).text
