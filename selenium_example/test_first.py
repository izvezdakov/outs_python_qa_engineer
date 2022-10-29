
def test_hello_selenium(driver):
    driver.get(url=driver.base_url)
    driver.save_screenshot('test.png')
    assert driver.title == 'Your Store'