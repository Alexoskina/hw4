from objects.catalog_page import CatalogPage
from objects.main_page import MainPage



def test_len_of_products_in_catalog(browser, url):
    browser.get(url + "index.php?route=product/category&path=33")
    assert len(browser.find_elements(*CatalogPage.CATALOG_ELEMENTS)) == 2


def test_check_products_in_catalog(browser, url):
    browser.get(url + "index.php?route=product/category&path=33")
    old_layout = browser.find_element(*CatalogPage.LAYOUT_CLASS).get_attribute("class").split(" ")[1]
    browser.find_element(*CatalogPage.LIST_VIEW_BTN).click()
    new_layout = browser.find_element(*CatalogPage.LAYOUT_CLASS).get_attribute("class").split(" ")[1]
    assert old_layout == "product-grid"
    assert new_layout == "product-list"


def test_name_of_catalog(browser, url):
    browser.get(url + "index.php?route=product/category&path=33")
    page_name = browser.find_element(*MainPage.PAGE_NAME).text
    catalog_name = browser.find_element(*CatalogPage.CATALOG_NAME).text
    assert page_name != catalog_name
