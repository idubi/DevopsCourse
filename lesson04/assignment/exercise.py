from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from utils.selenium_utils import load_path, get_selenium_driver, find_element, \
    click_element, get_element_value, set_element_value, get_cookies, del_cookies
from utils.config import get_logger
from logging import getLogger
import json

WEB_SITES = {
    "WALLA": {"URL": "https://walla.co.il"},
    "YNET": {"URL": "https://ynet.co.il"},
    "GOOGLE_TRANSLATE_HEB_2_ENG": {"URL": "https://translate.google.com",
                                   "HEB": '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea',
                                   "HEB_CLEAN": '//*[@id="ow73"]/div[1]/span/button/div[3]',
                                   "ENG": '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span',
                                   "COPY_TRANSLATION": '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[4]/div[2]/span[2]/button/div[3]',
                                   "TRANSLATION_ERROR_BUTTON": '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[7]/div[2]/button/span'
                                   },
    "YOUTUBE": {"URL": "https://www.youtube.com",
                "SEARCH_TEXT": '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input',
                "SEARCH_BUTTON": '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button',
                },
    "GOOGLE_TRANSLATE_CLEAN": {"URL": "https://translate.google.com",
                               "BY_FULL_XPATH": '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea',
                               "BY_PARTIAL_XPATH": '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea',
                               "BY_CLASS_NAME": 'er8xn'},
    "FACEBOOK": {"URL": "https://www.facebook.com",
                 "USER_NAME": '//*[@id="email"]',
                 "PASSWORD": '//*[@id="pass"]',
                 "LOG_IN_BUTTON": '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'},
    "GITHUB": {"URL": "https://github.com",
               "SEARCH_TEXT": '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]'
               }

}


def str_rtl(str):
    return str[::-1]


def web_sites_to_json():
    json_str = json.dumps(WEB_SITES)
    return json.loads(json_str)


def did_fail_for_translation_error(chrome_driver):
    translation_error = get_element_value(chrome_driver, web_sites_to_json().
                                          get('GOOGLE_TRANSLATE_HEB_2_ENG').get('TRANSLATION_ERROR_BUTTON'))
    if translation_error:
        get_logger().critical(f'\n -------------------------------------------------- \n |  ' \
                              '  FAILED OVER GOOGLE TRANSLATION ERROR !!!!   | \n ' \
                              ' -------------------------------------------------- \n')
        return True
    else:
        return False


def show_exercise_boundary(exercise_name, exercise_summery):
    get_logger().info(f'-------------------------------------- \n ================ {exercise_name} ================= ')
    if exercise_summery:
        get_logger().debug(f'\n \n ==> {exercise_summery}')

    get_logger().info(f'\n --------------------------------------')


def ex_01_02():
    show_exercise_boundary('ex_01_02',
                           f'open chrome and firefox with walla/ynet \n show webDriver parameters, and compare them. \n refresh them ')
    chrome_driver = get_selenium_driver("CHROME")
    firefox_driver = get_selenium_driver("FIREFOX")
    if not (chrome_driver and firefox_driver):
        get_logger().error('failed to load chrome and/or firefox')
        return False

    try:
        load_path(chrome_driver, web_sites_to_json().get('WALLA').get('URL'))

        chrome_name = chrome_driver.name
        chrome_title = chrome_driver.title
        chrome_url = chrome_driver.current_url
        chrome_session_id = chrome_driver.session_id
        get_logger().info(
            f'chrome site results : \n -> site ; {chrome_url} , \n -> title : {chrome_title} \n -> name : {chrome_name} \n --> session : {chrome_session_id} ')
        chrome_driver.refresh()
        get_logger().info(f'chrome site refreshed --> session : {chrome_session_id} ')

        load_path(firefox_driver, web_sites_to_json().get('YNET').get('URL'))
        firefox_name = firefox_driver.name
        firefox_title = firefox_driver.title
        firefox_url = firefox_driver.current_url
        firefox_session_id = firefox_driver.session_id

        # comparison :
        if firefox_url == chrome_url:
            print('same site')
        else:
            print('different sites')

        get_logger().info(
            f'chrome site results : \n -> site ; {firefox_url} , \n -> title : {firefox_title} \n -> name : {firefox_name} \n --> session : {firefox_session_id} ')
        firefox_driver.refresh()
        get_logger().info(f'firefox site refreshed --> session : {firefox_session_id} ')
    finally:
        chrome_driver and chrome_driver.quit()
        firefox_driver and firefox_driver.quit()


def ex_03():
    show_exercise_boundary('ex_03', 'does the element has the same locator in the other browse ?')
    get_logger().info("Yes  , it's the same")


def ex_04():
    show_exercise_boundary('ex_04', 'test google translate automation')
    driver = get_selenium_driver("FIREFOX")
    if driver:
        load_path(driver, web_sites_to_json().get('GOOGLE_TRANSLATE_HEB_2_ENG').get('URL'))
        phrase = "בוקר"
        heb_path = web_sites_to_json().get('GOOGLE_TRANSLATE_HEB_2_ENG').get('HEB')
        eng_path = web_sites_to_json().get('GOOGLE_TRANSLATE_HEB_2_ENG').get('ENG')

        set_element_value(driver, heb_path, phrase)

        translation = get_element_value(driver, eng_path, 5)
        get_logger().info(f'the meaning of {str_rtl(phrase)} is {translation}')
        if not translation:
            did_fail_for_translation_error(driver)
        # input('ex_04 ==> please type any key to continue')
        driver.quit()


def ex_05():
    show_exercise_boundary('ex_05', 'test youtube automation')
    driver = get_selenium_driver("FIREFOX")
    if driver:
        load_path(driver, web_sites_to_json().get('YOUTUBE').get('URL'))
        song_name = "devops with nana"
        set_element_value(driver, web_sites_to_json().get('YOUTUBE').get('SEARCH_TEXT'), song_name, 5)
        click_element(driver, web_sites_to_json().get('YOUTUBE').get('SEARCH_BUTTON'))
        # input('ex_05 ==> please type any key to continue')
        driver.quit()


def ex_06():
    show_exercise_boundary('ex_06', 'locate element in google translate using 3 different methods')
    driver = get_selenium_driver("CHROME")
    if driver:
        load_path(driver, web_sites_to_json().get('GOOGLE_TRANSLATE_CLEAN').get('URL'))

        by_xpath_path = web_sites_to_json().get('GOOGLE_TRANSLATE_CLEAN').get('BY_PARTIAL_XPATH')
        by_full_xpath_path = web_sites_to_json().get('GOOGLE_TRANSLATE_CLEAN').get('BY_FULL_XPATH')
        by_class_name_path = web_sites_to_json().get('GOOGLE_TRANSLATE_CLEAN').get('BY_CLASS_NAME')

        element_xpth = find_element(driver, by_xpath_path, 0, 'XPATH')
        element_fulll_xpth = find_element(driver, by_full_xpath_path, 0, 'XPATH')
        element_class_name = find_element(driver, by_class_name_path, 0, 'CLASS_NAME')

        get_logger().info(f'using xpath => {by_xpath_path} \n {element_xpth}')
        get_logger().info(f'using full xpath => {by_full_xpath_path} \n {element_fulll_xpth}')
        get_logger().info(f'using selector => {by_class_name_path} \n {element_class_name}')
        # input('ex_06 ==>please type any key to continue')
        driver.quit()


def ex_07():
    show_exercise_boundary('ex_07', 'login to facebook')
    # password = input("please type your facebook password:")
    password = "HAnt1989!!"
    driver = get_selenium_driver("CHROME")

    if driver:
        load_path(driver, web_sites_to_json().get('FACEBOOK').get('URL'))

        user_input_path = web_sites_to_json().get('FACEBOOK').get('USER_NAME')
        password_input_path = web_sites_to_json().get('FACEBOOK').get('PASSWORD')
        login_button_path = web_sites_to_json().get('FACEBOOK').get('LOG_IN_BUTTON')

        user_email = 'idubi.spam@gmail.com'

        set_element_value(driver, user_input_path, user_email, 5)
        set_element_value(driver, password_input_path, password, 0)
        click_element(driver, login_button_path)
        # input('ex_07 ==>please type any key to continue')
        driver.quit()


def ex_08():
    show_exercise_boundary('  ex_08 (Challenges) ', 'show cookies , delete them , and check it is really deleted')
    facebook_url = web_sites_to_json().get('FACEBOOK').get('URL')
    # selected_site = input(f"please type site name for cookies probing (default: {facebook_url}) :") or facebook_url
    selected_site = facebook_url
    driver = get_selenium_driver("CHROME")
    load_path(driver, selected_site)
    cookies = get_cookies(driver)
    if cookies:
        del_cookies(driver)
    # driver.refresh()
    cookies = get_cookies(driver)
    if cookies:
        get_logger().error('cookis are available , after deletion !!!!')
        return False
    else:
        get_logger().info('successfully deleted all cookies')
        return True


def ex_09():
    show_exercise_boundary('ex_09 (Challenges)', 'open github and search ... ')
    github_url = web_sites_to_json().get('GITHUB').get('URL')
    search_box_path = web_sites_to_json().get('GITHUB').get('SEARCH_TEXT')
    text_to_saerch = 'seleniuum'
    driver = get_selenium_driver("FIREFOX", True)
    if driver:
        load_path(driver, github_url)
        set_element_value(driver, search_box_path, text_to_saerch)
        set_element_value(driver, search_box_path, Keys.ENTER)
        # input('ex_09 ==>please type any key to continue')
        driver.quit()


def ex_10():
    show_exercise_boundary('ex_10 (Challenges)', 'load browsers without extensions')
    chrome_driver = get_selenium_driver("CHROME", True)
    firefox_driver = get_selenium_driver("FIREFOX", True)

    if chrome_driver and firefox_driver:
        load_path(chrome_driver, 'http://www.oracle-developer.net/')
        load_path(firefox_driver, 'http://www.oracle-developer.net/')
        # input()
    chrome_driver and chrome_driver.quit()
    firefox_driver and firefox_driver.quit()


def ex_11():
    show_exercise_boundary('ex_11 (Challenges)', 'Find a way to start a browser without extensions')
    get_logger().info("for a broser wihout extensions : \n " \
                      "for chrome : execute  'chrome --disable-extensions'   \n " \
                      "for firefox : create a profile without any extensins , name it no-extensions , and execute : 'firefox -P no-extensions' ")
