from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):

        self.wait.until(
            EC.element_to_be_clickable(
                self.USERNAME_INPUT)).send_keys(username)
        self.wait.until(
            EC.element_to_be_clickable(
                self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON)).click()
