from selenium.webdriver.common.by import By
from sixth_hw.page_objects.BasePage import BasePage


class MainPage(BasePage):
    _MENU = (By.CSS_SELECTOR, '#menu')
    _LOGO = (By.CSS_SELECTOR, '#logo')
    _SLIDESHOW = (By.CSS_SELECTOR, '#slideshow0')
    _SEARCH = (By.CSS_SELECTOR, '#search')
    _CART = (By.CSS_SELECTOR, '#cart')

    @property
    def menu(self):
        self.element(self._MENU)
        return self

    @property
    def logo(self):
        self.element(self._LOGO)
        return self

    @property
    def slideshow(self):
        self.element(self._SLIDESHOW)
        return self

    @property
    def search(self):
        self.element(self._SEARCH)
        return self

    @property
    def cart(self):
        self.element(self._CART)
        return self
