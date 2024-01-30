from selenium.webdriver.common.by import By
from .basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC

tensor_button_locator = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')
block_sila_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
popodrobnee_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
section_rabotaem_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[4]')
class TensorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url='https://tensor.ru/'):
        self.driver.get(url)
