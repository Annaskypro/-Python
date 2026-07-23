import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def test_navigation():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://httpbin.org/")
    sleep(5)
    # Найдите и кликните на ссылку HTML Form.
    click_HTML_form =driver.find_element(By.LINK_TEXT, "HTML form")
    click_HTML_form.click()
    sleep(2)
    # Проверьте, что URL изменился на /forms/post.
    assert "/forms/post" in driver.current_url
    # Вернитесь назад на главную страницу.
    driver.back()
    # Проверьте, что вернулись на исходный URL.
    assert "https://httpbin.org/" == driver.current_url
    driver.quit()
    