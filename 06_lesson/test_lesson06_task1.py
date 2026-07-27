from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    # 2. Найдите и нажмите на кнопку "Start"
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    # 3. Дождитесь появления текста "Hello World!"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "#finish"), "Hello World!"))
    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshots/test_lesson06_task1.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    element = driver.find_element(By.CSS_SELECTOR, "#finish").text
    assert element == "Hello World!"
    driver.quit()
