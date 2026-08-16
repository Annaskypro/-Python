from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа.

    Этот класс предоставляет методы для заполнения формы заказа,
    перехода к следующему шагу и получения итоговой суммы.
    """

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver) -> None:
        """
        Инициализация объекта CheckoutPage.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить форму оформления заказа: Имя='{first_name}',"
                 " Фамилия='{last_name}', Индекс='{postal_code}'")
    def fill_checkout_form(self, first_name: str, last_name: str,
                           postal_code: str) -> None:
        """
        Заполняет форму оформления заказа данными пользователя.

        Метод заполняет три поля: имя, фамилия и почтовый индекс.
        Перед вводом данных каждое поле ожидает, пока станет кликабельным.
        """
        with allure.step(f"Ввести имя: {first_name}"):
            self.wait.until(
                EC.element_to_be_clickable(
                    self.FIRST_NAME_INPUT)).send_keys(first_name)

        with allure.step(f"Ввести фамилию: {last_name}"):
            self.wait.until(
                EC.element_to_be_clickable(
                    self.LAST_NAME_INPUT)).send_keys(last_name)

        with allure.step(f"Ввести почтовый индекс: {postal_code}"):
            self.wait.until(
                EC.element_to_be_clickable(
                    self.POSTAL_CODE_INPUT)).send_keys(postal_code)

        allure.attach(
            f"Имя: {first_name}, Фамилия: {last_name}, Индекс: {postal_code}",
            name="Данные пользователя",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Нажать кнопку 'Continue'")
    def click_continue(self) -> None:
        """
        Нажимает на кнопку "Continue" для перехода
        к следующему шагу оформления заказа.

        Метод ожидает, пока кнопка станет кликабельной, затем выполняет клик.
        После клика происходит переход на страницу подтверждения заказа.
        """
        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON)).click()

    @allure.step("Получить текстовое значение итоговой суммы")
    def get_total(self) -> str:
        """
        Получает текстовое значение итоговой суммы заказа.

        Метод ожидает появления элемента с итоговой суммой
            и возвращает его текст.
        """
        with allure.step("Ожидать появления элемента с итоговой суммой"):
            # ✅ Правильно: ищем элемент с итоговой суммой
            total_element = self.wait.until(
                EC.presence_of_element_located(self.TOTAL_LABEL)
            )

        with allure.step("Получить текст итоговой суммы"):
            total_text = total_element.text
            allure.attach(
                total_text,
                name="Итоговая сумма",
                attachment_type=allure.attachment_type.TEXT
            )
            return total_text

    @allure.step("Получить итоговую сумму в виде числа")
    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа в виде числа с плавающей точкой.

        Метод вызывает get_total() для получения текстового значения,
        затем извлекает числовое значение и преобразует его в float.
        """
        with allure.step("Получить текстовое значение итоговой суммы"):
            total_text = self.get_total()

        with allure.step(
                f"Извлечь числовое значение из строки:'{total_text}'"):
            total_price = float(total_text.replace("Total: $", ""))
            allure.attach(
                str(total_price),
                name="Итоговая сумма (число)",
                attachment_type=allure.attachment_type.TEXT
            )
            return total_price
