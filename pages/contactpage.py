from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class ContactsPage(BasePage):
    def go_to_tensor(self):
        self.driver.get("https://sbis.ru/")
        contacts_section_locator = (By.LINK_TEXT, "Контакты")
        self.click_element(contacts_section_locator)
        tensor_banner_locator = (By.LINK_TEXT, "Тензор")
        self.click_element(tensor_banner_locator)
        tensor_url_locator = (EC.url_to_be, "https://tensor.ru/")
        self.wait_for_element(tensor_url_locator)


driver = webdriver.Chrome()
