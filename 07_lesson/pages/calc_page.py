from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_plus = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_equals = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def open_calc(self, url):
        self.driver.get(url)

    def delay_field(self, time_delay):
        delay_input = self.driver.find_element(*self.DELAY)
        delay_input.clear()
        delay_input.send_keys(str(time_delay))

    def button_calc(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_7)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_plus)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_8)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_equals)).click()

    def get_result_with_expected(self, expected_value):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT, expected_value)
            )
        return self.driver.find_element(*self.RESULT).text
