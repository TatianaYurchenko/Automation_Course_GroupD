import time
# позволяет имитировать нажатие на клавиатуру
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Test_google:
    def test_find_title(self, driver):
        # в DOM в хедерах есть тэг title. Для роверки что перешли на правильную страницу
        driver.get("https://www.google.com")
        title = driver.title
        assert title == "Google"
        print(title)



    def test_find_fill(self, driver):
        # найти поле по селектору заполнить его
        locator = (By.CSS_SELECTOR, "textarea[class='gLFyf']")
        driver.get("https://www.google.com")
        input_fild = driver.find_element(*locator)
        input_fild.send_keys("Python")
        # имитирует нажатие на ENTER
        input_fild.send_keys(Keys.ENTER)

class Test_magento:
    def test_by(self, driver):
        locator = (By.CSS_SELECTOR, "a[id='ui-id-8']")
        driver.get("https:magento.softwaretestingboard.com/")
        element = driver.find_element(*locator)
        element.click()
        driver.back()
        driver.forward()
        driver.refresh()

    def test_open_browser(self, driver):
        driver.get("https:magento.softwaretestingboard.com/")
        time.sleep(3)

class Test_demoqa:
    def test_click_buttons(self, driver):
        driver.get("https://demoqa.com/buttons")
        button = driver.find_element(By.XPATH, '(//button[@type="button"])[4]')
        button.click()
        message = driver.find_element(By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')
        text = message.text
        assert text == 'You have done a dynamic click'

    def test_double_click_buttons(self, driver):
        driver.get("https://demoqa.com/buttons")
        button = driver.find_element(By.XPATH, '(//button[@type="button"])[2]')
        actions = ActionChains(driver)
        actions.double_click(button)
        actions.perform()
        message = driver.find_element(By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
        text = message.text
        assert text == 'You have done a double click'

    def test_right_click_buttons(self, driver):
        driver.get("https://demoqa.com/buttons")
        button = driver.find_element(By.XPATH, '(//button[@type="button"])[3]')
        actions = ActionChains(driver)
        actions.context_click(button)
        actions.perform()
        message = driver.find_element(By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
        text = message.text
        assert text == 'You have done a right click'
