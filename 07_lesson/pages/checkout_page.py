from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.element_to_be_clickable(
                self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.wait.until(
            EC.element_to_be_clickable(
                self.LAST_NAME_INPUT)).send_keys(last_name)
        self.wait.until(
            EC.element_to_be_clickable(
                self.POSTAL_CODE_INPUT)).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON)).click()

    def get_total(self):
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return total_element.text

    def get_total_price(self):
        total_text = self.get_total()
        # Извлекаем число из строки "Total: $58.29"
        return float(total_text.replace("Total: $", ""))
