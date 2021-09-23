from objects.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_main_page(browser, url):
    browser.get(url)
    assert browser.title == "Your Store"


def test_check_visibility_of_search_button(browser, url):
    browser.get(url)
    browser.find_element(*MainPage.BUTTON_SEARCH)


def test_check_visibility_of_search_input(browser, url):
    browser.get(url)
    browser.find_element(*MainPage.INPUT_SEARCH)


def test_check_visibility_of_macbookair_banner(browser, url):
    browser.get(url)
    WebDriverWait(browser, 4).until(ec.visibility_of_element_located((By.XPATH, MainPage.BANNER_MACBOOKAIR)))


def test_len_of_product_thumbs(browser, url):
    browser.get(url)
    product_thumbs = browser.find_elements(*MainPage.PRODUCT_THUMB)
    assert len(product_thumbs) == 4
