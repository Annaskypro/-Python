from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_bonigarcia():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
    driver.find_element(
        By.CSS_SELECTOR, "[class='btn btn-outline-primary mt-3']").click()
    zip_code = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "zip-code")))
    assert "danger" in zip_code.get_attribute("class")
    fields = ["first-name", "last-name", "address", "e-mail",
              "phone", "city", "country", "job-position", "company"]
    for field_id in fields:
        field = driver.find_element(By.ID, field_id)
        assert "success" in field.get_attribute("class")
    driver.quit()
