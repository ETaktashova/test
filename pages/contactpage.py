from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver

contacts_buttton_locator = (By.LINK_TEXT, 'Контакты')

class ContactsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url= 'https://sbis.ru/'):
        self.driver.get(url)


