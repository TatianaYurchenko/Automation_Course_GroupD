# здесь будут: фикстура которая запускает наш драйвер
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# фикстура которая запускает наш драйвер
@pytest.fixture(scope='function')
def driver():
    chrom_options = webdriver.ChromeOptions()

    # == варианты загрузки драйвера==
    # 1 вариант три вида загрузки страницы normal по умолчанию, none - ничего не ждет , eager загружает только DOM- дерево
    # chrom_options.page_load_strategy = 'normal'
    # самый правильный для задания размеров
    # chrom_options.add_argument("--window-size=1500, 900")
    chrom_options.add_argument("--start-maximized")
    # # chrom_options.add_argument("--incognito")
    # # 2 вариант безголовый режим без открытия браузера полезен в прогоне в CI CD
    # chrom_options.add_argument("--headless")
    # # 3 вариант зайти в режиме инкогнито
    # chrom_options.add_argument("--incognito")
    # #  ИГНОР сертификатов
    # chrom_options.add_argument("--ignor-certificate-errors")
    # =====
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrom_options)

    yield driver
    driver.quit()