import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from objects.product_page import ProductPage


@pytest.mark.parametrize("product_id,cart_total", [(43, "2 item(s) - $1,204.00"), (48, "2 item(s) - $244.00")])
def test_product_page(browser, url, product_id, cart_total):
    browser.get(url + f"index.php?route=product/product&product_id={product_id}")

    # add 2 items
    qty_input = browser.find_element(*ProductPage.QUANTITY_ITEMS_INPUT)
    qty_input.clear()
    qty_input.send_keys(2)
    assert qty_input.get_attribute("value") == '2'

    browser.find_element(*ProductPage.SUBMIT_BUTTON).click()
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located(ProductPage.ADD_TO_CART_ALERT))
    assert browser.find_element(*ProductPage.CART_TOTAL_ROW).text == cart_total
