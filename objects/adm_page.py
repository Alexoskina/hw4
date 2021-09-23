from selenium.webdriver.common.by import By


class Adm_Page:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    HEADER_TITLE = (By.CSS_SELECTOR, ".panel-title")
    LOG_BTN = (By.CSS_SELECTOR, ".btn.btn-primary")
    ERR_MESSAGE = "//div[@class='alert alert-danger alert-dismissible']"