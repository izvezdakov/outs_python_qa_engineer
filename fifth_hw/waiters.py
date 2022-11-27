from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element_until(by_selector_couple, driver, timeout=1,
                       expectation_method=EC.visibility_of_element_located):
    try:
        return WebDriverWait(driver=driver, timeout=timeout).until(expectation_method(by_selector_couple))
    except TimeoutError:
        driver.save_screenshot(f'{driver.session_id}.png')
        raise AssertionError(f'Не дождался {expectation_method} элемента {by_selector_couple}.')
