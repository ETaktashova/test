from .basepage import BasePage
from selenium.webdriver.common.by import By


contacts_buttton_locator = (By.LINK_TEXT, 'Контакты')
my_region_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
kamchatka_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
partners_locator_my_reg = (
    By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
partners_locator_kamchat_list = (
    By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
locator_kamchat_reg_inregions_list = (
    By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')
class ContactsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url= 'https://sbis.ru/'):
        self.driver.get(url)


