import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_navigation():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://httpbin.org/links/10")
    links = driver.find_elements(By.TAG_NAME, "a")
    assert len (links) == 9
    for link in links: assert link.is_displayed();
    assert "1" in links[0].text
    driver.quit()