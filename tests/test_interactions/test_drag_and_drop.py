import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

DRAG = (By.CSS_SELECTOR, "div[id='draggable']")
DROP = (By.CSS_SELECTOR, "div[id='droppable']")
