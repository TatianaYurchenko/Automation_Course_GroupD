import time
from data.example import split_text_box
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

YES_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio'")
IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
TEXT_YES = (By.CSS_SELECTOR, "span[class='text-success']")

def test_check_radio_button(driver):
    driver.get('https://demoqa.com/radio-button')
    driver.find_element(*YES_BUTTON).click()
    text = driver.find_element(*TEXT_YES).text
    print(text)
    assert text =="Yes"
    driver.find_element(*IMPRESSIVE_BUTTON).click()
    text = driver.find_element(*TEXT_YES).text
    assert text == "Impressive"
    print(text)


