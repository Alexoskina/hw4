from selenium.webdriver.common.by import By


class CatalogPage:
    CATALOG_NAME = (By.CSS_SELECTOR, ".row > div > h2")
    CATALOG_ELEMENTS = (By.XPATH, "//div[@class='product-thumb']")
    BOTTOM_COUNTER = (By.CSS_SELECTOR, ".text-right")
    LAYOUT_CLASS = (By.CSS_SELECTOR, ".product-layout")
    LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")