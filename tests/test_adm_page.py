from objects.adm_page import Adm_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_placeholders(browser, url):
    browser.get(url + "admin")
    assert browser.find_element(*Adm_Page.USERNAME_INPUT).get_attribute("placeholder") == "Username"
    assert browser.find_element(*Adm_Page.PASSWORD_INPUT).get_attribute("type") == "password"


def test_header(browser, url):
    browser.get(url + "admin")
    assert browser.find_element(*Adm_Page.HEADER_TITLE).text == "Please enter your login details."


def test_inputs(browser, url):
    browser.get(url + "admin")
    user_name = browser.find_element(*Adm_Page.USERNAME_INPUT)
    user_name.send_keys("username")
    pass_word = browser.find_element(*Adm_Page.PASSWORD_INPUT)
    pass_word.send_keys("passw")
    browser.find_element(*Adm_Page.LOG_BTN).click()
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, Adm_Page.ERR_MESSAGE)))


def test_error_login(browser, url):
    browser.get(url + "admin")
    browser.find_element(*Adm_Page.LOG_BTN).click()
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, Adm_Page.ERR_MESSAGE)))

