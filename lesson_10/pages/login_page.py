from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """
    Класс для работы со страницей авторизации (логина).

    Этот класс предоставляет методы для открытия страницы логина
    и выполнения процесса авторизации пользователя.
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """
        Инициализация объекта LoginPage.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации: {url}")
    def open(self, url: str) -> None:
        """
        Открывает страницу авторизации по указанному URL.
        """
        with allure.step(f"Перейти по URL: {url}"):
            self.driver.get(url)
            allure.attach(
                url,
                name="URL страницы",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.step("Выполнить авторизацию с логином '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя с указанными учетными данными.

        Метод последовательно вводит имя пользователя и пароль,
        затем нажимает кнопку входа. Каждое действие выполняется
        после ожидания готовности элемента (кликабельности).
        """

        with allure.step(f"Ввести имя пользователя: {username}"):
            self.wait.until(
                EC.element_to_be_clickable(
                    self.USERNAME_INPUT)).send_keys(username)

        with allure.step("Ввести пароль"):
            self.wait.until(
                EC.element_to_be_clickable(
                    self.PASSWORD_INPUT)).send_keys(password)

        with allure.step("Нажать кнопку входа"):
            self.wait.until(
                EC.element_to_be_clickable(
                    self.LOGIN_BUTTON)).click()

        allure.attach(
            f"Логин: {username}, Пароль: {password}",
            name="Учетные данные",
            attachment_type=allure.attachment_type.TEXT
        )
