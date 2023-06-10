from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

WEB_DRIVER_PATH = '~/Downloads/chromedriver'


def get_selenium_driver():
    return webdriver.Chrome(service=Service(executable_path=WEB_DRIVER_PATH))


def load_path(driver, site_path):
    driver.get(site_path)
    while not driver.execute_script("return document.readyState")=="complete":
        time.sleep(0.3)
    return driver


def set_element_value(web_driver, path, value):
    web_driver.find_element(By.XPATH, path).send_keys(value)


def click_element(web_driver, path):
    web_driver.find_element(By.XPATH, path).click()


def get_element_value(web_driver, path):
    return web_driver.find_element(By.XPATH, path).text
