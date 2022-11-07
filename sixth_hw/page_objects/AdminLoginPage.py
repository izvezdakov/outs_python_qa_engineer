from selenium.webdriver.common.by import By
from sixth_hw.page_objects.BasePage import BasePage


class AdminLoginPage(BasePage):
    
    _INPUT_USERNAME = (By.CSS_SELECTOR, '#input-username')
    _INPUT_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    _HELP_BLOCK = (By.XPATH, "//*[@class='help-block']")
    _LOGIN_BTN = (By.XPATH, "//*[@class='btn btn-primary']")
    _FOOTER = (By.CSS_SELECTOR, "#footer")

    @property
    def form_input_username(self):
        self.element(self._INPUT_USERNAME)
        return self

    @property
    def form_input_password(self):
        self.element(self._INPUT_PASSWORD)
        return self

    @property
    def help_block(self):
        self.element(self._HELP_BLOCK)
        return self

    @property
    def btn_login(self):
        self.element(self._LOGIN_BTN)
        return self

    @property
    def footer(self):
        self.element(self._FOOTER)
        return self
