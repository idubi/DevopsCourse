from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# WEB_DRIVER_PATH = '~/Downloads/chromedriver'
WEB_DRIVER_PATH_CHROME = 'D:\\projects\\DevopsCourse\\venv\\chromium\\chromedriver.exe'


def get_selenium_driver(browser_type):
    if browser_type == "CHROME":
        return webdriver.Chrome(service=Service(executable_path=WEB_DRIVER_PATH_CHROME))
    elif browser_type == "FIREFOX":
        return webdriver.Firefox()


def load_path(driver, site_path):
    driver.get(site_path)
    status = driver.execute_script("return document.readyState")
    while not status=="complete":
        print(f'status of page is  {status}'  )
        time.sleep(0.3)
        status = driver.execute_script("return document.readyState")
        # print(f'page loaded successfully  {driver.}'  )
    return driver


def set_element_value(web_driver, path, value):
    web_driver.find_element(By.XPATH, path).send_keys(value)


def click_element(web_driver, path):
    web_driver.find_element(By.XPATH, path).click()


def get_element_value(web_driver, path):
    return web_driver.find_element(By.XPATH, path).text
