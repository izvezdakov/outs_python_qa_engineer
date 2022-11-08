from selenium.webdriver.common.by import By
from sixth_hw.page_objects.BasePage import BasePage


class AdminPage(BasePage):
    _MENU_CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    _MENU_CATALOG_PRODUCTS = (By.CSS_SELECTOR, "li:nth-child(2)")
    _BTN_ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "[data-original-title='Add New']")

    @property
    def menu_catalog(self):
        return self.element(self._MENU_CATALOG)

    @property
    def menu_catalog__products(self):
        return self.element_in_element(parent_locator=self._MENU_CATALOG, child_locator=self._MENU_CATALOG_PRODUCTS)

    @property
    def btn_add_new_product(self):
        return self.element(self._BTN_ADD_NEW_PRODUCT)
