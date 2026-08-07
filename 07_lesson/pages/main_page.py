from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_T_SHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_all_items_to_cart(self):

        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD)).click()
        self.wait.until(
            EC.element_to_be_clickable(self.BOLT_T_SHIRT_ADD)).click()
        self.wait.until(EC.element_to_be_clickable(self.ONESIE_ADD)).click()
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()
