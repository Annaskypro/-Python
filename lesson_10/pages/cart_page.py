from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """
    Класс для работы со страницей корзины интернет-магазина.

    Этот класс предоставляет методы для взаимодействия с элементами корзины,
    включая подсчет товаров и переход к оформлению заказа.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver) -> None:
        """
        Инициализация объекта CartPage.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Возвращает количество товаров в корзине.

        Метод находит все элементы, добавленные в корзину
            и подсчитывает их количество.
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self) -> None:
        """
        Нажимает на кнопку оформления заказа.

        Метод ожидает, пока кнопка "Оформить заказ" станет кликабельной,
        после чего выполняет клик по ней.
        """

        with allure.step("Ожидать, пока кнопка 'Checkout' "
                         "станет кликабельной"):
            checkout_button = self.wait.until(
                EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
            )
        with allure.step("Выполнить клик по кнопке 'Checkout'"):
            checkout_button.click()
            allure.attach(
                "Клик выполнен",
                name="Действие",
                attachment_type=allure.attachment_type.TEXT
            )
