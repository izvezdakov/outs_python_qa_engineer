from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from fifth_hw.waiters import wait_element_until


class MainPage:
    MENU = (By.CSS_SELECTOR, '#menu')
    LOGO = (By.CSS_SELECTOR, '#logo')
    SLIDESHOW = (By.CSS_SELECTOR, '#slideshow0')
    SEARCH = (By.CSS_SELECTOR, '#search')
    CART = (By.CSS_SELECTOR, '#cart')


def test_check_elements_on_main_page(driver):
    driver.get(driver.base_url + '')
    for selector, timeout in [
        (MainPage.MENU, 1),
        (MainPage.LOGO, 0.5),
        (MainPage.SLIDESHOW, 0.6),
        (MainPage.SEARCH, 1),
        (MainPage.CART, 1),
    ]:
        wait_element_until(by_selector_couple=selector,
                           driver=driver,
                           timeout=timeout,
                           expectation_method=EC.visibility_of_element_located)


class ProductPage:
    ADDTOCART_BTN = (By.CSS_SELECTOR, '#button-cart')
    DESCRIPTION = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/ul[2]/li[1]/a')
    SHARE_BTN = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[3]/div/a[4]/a[1]')
    ADD_TO_WISH_BTN = (By.XPATH, "//*[@class='fa fa-heart']")
    THUMBNAILS = (By.XPATH, "//*[@class='thumbnails']")


def test_check_elements_on_product_page(driver):
    driver.get(driver.base_url + 'iphone')

    wait_element_until(by_selector_couple=ProductPage.ADDTOCART_BTN,
                       driver=driver,
                       timeout=1,
                       expectation_method=EC.visibility_of_element_located)

    wait_element_until(by_selector_couple=ProductPage.DESCRIPTION,
                       driver=driver,
                       timeout=1,
                       expectation_method=EC.visibility_of_element_located)

    WebDriverWait(driver=driver, timeout=0.1). \
        until(EC.text_to_be_present_in_element(ProductPage.DESCRIPTION, 'Description'))

    wait_element_until(by_selector_couple=ProductPage.SHARE_BTN,
                       driver=driver,
                       timeout=6,
                       expectation_method=EC.visibility_of_element_located)

    wait_element_until(by_selector_couple=ProductPage.ADD_TO_WISH_BTN,
                       driver=driver,
                       timeout=6,
                       expectation_method=EC.visibility_of_element_located)

    wait_element_until(by_selector_couple=ProductPage.THUMBNAILS,
                       driver=driver,
                       timeout=6,
                       expectation_method=EC.visibility_of_element_located)
