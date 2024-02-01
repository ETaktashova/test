from pages.basepage import BasePage

class ContactsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url= 'https://sbis.ru/'):
        self.driver.get(url)


