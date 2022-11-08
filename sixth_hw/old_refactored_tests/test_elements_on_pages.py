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
    product_page = ProductPage(driver)
    assert product_page.thumbnails
    assert product_page.btn_share
    assert product_page.btn_add_to_cart
    assert product_page.btn_add_to_wish
    assert product_page.description


def test_check_elements_on_admin_login_page(driver):
    driver.get(driver.base_url + 'admin')
    admin_login_page = AdminLoginPage(driver)
    assert admin_login_page.footer
    assert admin_login_page.form_input_password
    assert admin_login_page.form_input_username
    assert admin_login_page.btn_login
    assert admin_login_page.help_block


def test_check_elements_on_register_page(driver):
    driver.get(driver.base_url + 'index.php?route=account/register')
    register_page = RegisterPage(driver)
    assert register_page.input_firstname
    assert register_page.input_lastname
    assert register_page.input_password
    assert register_page.input_telephone
    assert register_page.input_email


def test_check_elements_on_catalog_page(driver):
    driver.get(driver.base_url + 'desktops')
    catalog_page = CatalogPage(driver)
    assert catalog_page.column_left
    assert catalog_page.content
    assert catalog_page.password
    assert catalog_page.product_category
    assert catalog_page.sortby
