from utils.selenium_utils import click_element,get_element_value,set_element_value,load_path,get_selenium_driver


def ex_01_02():
    chrome_driver = get_selenium_driver("CHROME")
    load_path(chrome_driver,'https://walla.co.il')
    firefox_driver = get_selenium_driver("FIREFOX")
    load_path(firefox_driver,'https://ynet.co.il')
    chrome_title = chrome_driver.title
    firefox_title = firefox_driver.title
    # firefox_driver.refresh()
    # chrome_driver.refresh()
    # firefox_site_name=firefox_driver.name
    # chrome_site_name=chrome_driver.name
    chrome_driver.quit()
    firefox_driver.quit()
ex_01_02()