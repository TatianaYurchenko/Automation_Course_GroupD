import time
# позволяет имитировать нажатие на клавиатуру
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def test_find_title(driver):
    # в DOM в хедерах есть тэг title. Для роверки что перешли на правильную страницу
    driver.get("https://www.google.com")
    title = driver.title
    assert title == "Google"
    print(title)



def test_find_fill(driver):
    # найти поле по селектору заполнить его
    locator = (By.CSS_SELECTOR, "textarea[class='gLFyf']")
    driver.get("https://www.google.com")
    input_fild = driver.find_element(*locator)
    input_fild.send_keys("Python")
    # имитирует нажатие на ENTER
    input_fild.send_keys(Keys.ENTER)

def test_open_browser(driver):
    driver.get("https:magento.softwaretestingboard.com/")
    time.sleep(3)

def test_by(driver):
    locator = (By.CSS_SELECTOR, "a[id='ui-id-8']")
    driver.get("https:magento.softwaretestingboard.com/")
    element = driver.find_element(*locator)
    element.click()
    driver.back()
    driver.forward()
    driver.refresh()