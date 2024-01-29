from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.driver.find_element(locator)
        element.click()

    def assert_element_displayed(self, locator):
        element = self.driver.find_element(*locator)
        assert element.is_displayed()
