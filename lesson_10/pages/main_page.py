from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """
    Класс для работы с главной страницей интернет-магазина.

    Этот класс предоставляет методы для добавления товаров в корзину
    и перехода в корзину для оформления заказа.
    """

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_T_SHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver):
        """
        Инициализация объекта MainPage.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить все товары в корзину и перейти в корзину")
    def add_all_items_to_cart(self) -> None:
        """
        Добавляет все выбранные товары в корзину и переходит в корзину.

        Метод последовательно выполняет следующие действия:
        1. Добавляет рюкзак (Sauce Labs Backpack) в корзину
        2. Добавляет футболку (Sauce Labs Bolt T-Shirt) в корзину
        3. Добавляет комбинезон (Sauce Labs Onesie) в корзину
        4. Нажимает на кнопку корзины для перехода на страницу корзины

        Каждое действие выполняется после ожидания готовности
        элемента (кликабельности).
        """

        with allure.step("Добавить рюкзак (Sauce Labs Backpack) в корзину"):
            self.wait.until(EC.element_to_be_clickable(
                self.BACKPACK_ADD)).click()
            allure.attach(
                "Sauce Labs Backpack добавлен",
                name="Товар",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(
                "Добавить футболку (Sauce Labs Bolt T-Shirt) в корзину"):
            self.wait.until(
                EC.element_to_be_clickable(self.BOLT_T_SHIRT_ADD)).click()
            allure.attach(
                "Sauce Labs Bolt T-Shirt добавлен",
                name="Товар",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Добавить комбинезон (Sauce Labs Onesie) в корзину"):
            self.wait.until(EC.element_to_be_clickable(
                self.ONESIE_ADD)).click()
            allure.attach(
                "Sauce Labs Onesie добавлен",
                name="Товар",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Перейти в корзину"):
            self.wait.until(EC.element_to_be_clickable(
                self.CART_BUTTON)).click()
            allure.attach(
                "Переход на страницу корзины",
                name="Действие",
                attachment_type=allure.attachment_type.TEXT
            )
