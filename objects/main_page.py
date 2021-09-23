from selenium.webdriver.common.by import By


class MainPage:
    INPUT_SEARCH = (By.XPATH, "//input[@name='search']")
    BUTTON_SEARCH = (By.XPATH, "//span[@class='input-group-btn']/button")
    PRODUCT_THUMB = (By.CSS_SELECTOR, ".product-thumb")
    BANNER_MACBOOKAIR = "//div[@class='swiper-slide text-center swiper-slide-active']/img[@alt='MacBookAir']"
    PAGE_NAME = (By.CSS_SELECTOR, "#logo")