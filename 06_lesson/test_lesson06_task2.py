from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_session_storage_auth():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "MDk3NmNiMDQtN2Q0Mi00MDljLTk1MDgtMmMxNDJiYzI5ODMy",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/annaskypro")
    current_url1 = driver.current_url
    driver.delete_all_cookies()
    driver.add_cookie({
        "name": "SESSION",
        "value": "NzMxMjBkNzktMDczZC00YjBmLWJjZTktZjI0ZDA2M2Q4YTI0",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/ann_makedonskaya")
    current_url2 = driver.current_url
    assert current_url1 != current_url2
    driver.quit()
