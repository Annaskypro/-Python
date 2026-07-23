from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_navigation():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://httpbin.org/forms/post")
    sleep(2)
    driver.find_element(By.NAME, "custname").send_keys("Anna")
    sleep(2)
    driver.find_element(
        By.XPATH,
        "//button[contains(text(), 'Submit order')]").click()
    sleep(2)
    assert "https://httpbin.org/post" == driver.current_url
    sleep(2)
    driver.quit()
