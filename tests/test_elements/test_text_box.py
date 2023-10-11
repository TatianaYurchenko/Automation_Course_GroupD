
import time
from data.example import split_text_box
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
TEXT = (By.CSS_SELECTOR, "div[class='border col-md-12 col-sm-12']")

def test_fill_text_box(driver):
    driver.get("https://demoqa.com/text-box")
    driver.find_element(*FULL_NAME).send_keys("Tatiana")
    driver.find_element(*EMAIL).send_keys("Tatiana@mail.com")
    driver.find_element(*CURRENT_ADDRESS).send_keys("Tatiana")
    driver.find_element(*PERMANENT_ADDRESS).send_keys("Tatiana")
    driver.find_element(*BUTTON_SUBMIT).send_keys("Tatiana")
    time.sleep(2)
    driver.find_element(*BUTTON_SUBMIT).click()
    text_list = driver.find_elements(*TEXT)

    text1 = [i.text for i in text_list]
    text = split_text_box(text1)
    print(text)


