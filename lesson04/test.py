from lesson04.tip_calc.selenium.celenium_utils import load_path, get_element_value, click_element, \
    set_element_value, get_selenium_driver

# PATH = 'http://localhost:63342/DevopsCourse/lesson04/tip_calc/index.html'
PATH = 'file:///Users/idubim/PycharmProjects/pythonProject/DevopsCourse/lesson04/tip_calc/resources' \
       '/tip_calculator/index.html'

BILL_AMOUNT_SELECTOR = '//*[@id="billamt"]'
SERVICE_OPTION_SELECTOR = '//*[@id="serviceQual"]/option[4]'
PEOPLE_AMOUNT_SELECTOR = '//*[@id="peopleamt"]'
BUTTON_SELECTOR = '//*[@id="calculate"]'
TIP_AMOUNT = '//*[@id="tip"]'

driver = get_selenium_driver()
load_path(driver, PATH)


set_element_value(driver, PEOPLE_AMOUNT_SELECTOR, 45)
set_element_value(driver, BILL_AMOUNT_SELECTOR, 300)
click_element(driver, SERVICE_OPTION_SELECTOR)
click_element(driver, BUTTON_SELECTOR)

calculated_amount = get_element_value(driver, TIP_AMOUNT)
assert (calculated_amount == '1.00')


