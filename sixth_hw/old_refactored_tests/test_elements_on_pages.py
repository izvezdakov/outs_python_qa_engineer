from sixth_hw.page_objects.AdminLoginPage import AdminLoginPage
from sixth_hw.page_objects.CatalogPage import CatalogPage
from sixth_hw.page_objects.MainPage import MainPage
from sixth_hw.page_objects.ProductPage import ProductPage
from sixth_hw.page_objects.RegisterPage import RegisterPage


def test_check_elements_on_main_page(driver):
    driver.get(driver.base_url + '')
    main_page = MainPage(driver)
    assert main_page.menu
    assert main_page.logo
    assert main_page.slideshow
    assert main_page.search
    assert main_page.cart


def test_check_elements_on_product_page(driver):
    driver.get(driver.base_url + 'iphone')
    main_page = ProductPage(driver)
    assert main_page.thumbnails
    assert main_page.btn_share
    assert main_page.btn_add_to_cart
    assert main_page.btn_add_to_wish
    assert main_page.description


def test_check_elements_on_admin_login_page(driver):
    driver.get(driver.base_url + 'admin')
    main_page = AdminLoginPage(driver)
    assert main_page.footer
    assert main_page.form_input_password
    assert main_page.form_input_username
    assert main_page.btn_login
    assert main_page.help_block


def test_check_elements_on_register_page(driver):
    driver.get(driver.base_url + 'index.php?route=account/register')
    main_page = RegisterPage(driver)
    assert main_page.input_firstname
    assert main_page.input_lastname
    assert main_page.input_password
    assert main_page.input_telephone
    assert main_page.input_email


def test_check_elements_on_catalog_page(driver):
    driver.get(driver.base_url + 'desktops')
    main_page = CatalogPage(driver)
    assert main_page.column_left
    assert main_page.content
    assert main_page.password
    assert main_page.product_category
    assert main_page.sortby
