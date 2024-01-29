import pytest
from selenium import webdriver
from pages.contactpage import ContactsPage
from pages.tensorpage import TensorPage


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


# def test_scenario(setup):
#     driver = setup
#     contacts_page = ContactsPage(driver)
#     contacts_page.go_to_tensor()

#     tensor_page = TensorPage(driver)
#     tensor_page.check_sila_v_lyudyah()
#     tensor_page.go_to_about()
#     tensor_page.check_work_photos()


# test_scenario(setup)
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWebsite:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_sbis_to_tensor(self):
        # Открываем сайт https://sbis.ru/
        self.driver.get('https://sbis.ru/')

        # Переходим в раздел "Контакты"
        contacts = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Контакты')))
        contacts.click()

        # Находим баннер Тензор и кликаем по нему
        tensor_banner = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(((By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor'))))
        tensor_banner.click()

        # Переходим на сайт https://tensor.ru/
        assert self.driver.current_url == 'https://tensor.ru/'

    def test_tensor_page(self):
        # Открываем сайт https://tensor.ru/
        self.driver.get('https://tensor.ru/')

        # Проверяем, что есть блок "Сила в людях"
        strength_in_people = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'strength-in-people')))
        assert strength_in_people is not None

        # Переходим в "Подробнее" и проверяем URL
        details = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Подробнее')))
        details.click()

        assert self.driver.current_url == 'https://tensor.ru/about'

        # Проверяем размеры фотографий в разделе "Работаем"
        images = self.driver.find_elements(
            By.XPATH, '//div[@id="work-with-us"]//img')
        heights = {image.size['height'] for image in images}
        widths = {image.size['width'] for image in images}
        assert len(heights) == 1 and len(widths) == 1


test = TestWebsite()
test.setup_method()
test.test_sbis_to_tensor()
test.test_tensor_page()
