import pytest
from pages.tensorpage import TensorPage, tensor_button_locator, block_sila_locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contactpage import ContactsPage, contacts_buttton_locator
driver=webdriver.Chrome()
# Проверяю переход на tensor.ru через контакты и  баннер "тензор"
# def test_tensor_banner():
#     contacts = ContactsPage(driver)
#     contacts.open()
#     contacts.find(contacts_buttton_locator).click()
#     contacts.find(tensor_button_locator).click()
#     WebDriverWait(contacts.driver, 10).until(EC.number_of_windows_to_be(2))
#     # Получаем список идентификаторов вкладок
#     window_handles = contacts.driver.window_handles
#     # Переключаемся на последнюю открытую вкладку
#     contacts.driver.switch_to.window(window_handles[-1])
#     expected_url = "https://tensor.ru/"
#     actual_url = contacts.driver.current_url
#     assert actual_url == expected_url

# # Проверить, что есть блок "Сила в людях"
# def test_strength_in_people():
#     sila = TensorPage(driver)
#     sila.wait_for_element(block_sila_locator)
#     assert sila.find(block_sila_locator), "Блок 'Сила в людях' не найден на странице"

# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
# https://tensor.ru/about
popodrobnee_locator = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
def test_url_tensor_about():
    popodrobnee = TensorPage(driver)
    popodrobnee.open()
    popodrobnee.find(popodrobnee_locator).click()
    # WebDriverWait(popodrobnee.driver, 10).until(EC.number_of_windows_to_be(2))
    # Получаем список идентификаторов вкладок
    # window_handles = popodrobnee.driver.window_handles
    # Переключаемся на последнюю открытую вкладку
    # popodrobnee.driver.switch_to.window(window_handles[-1])
    expected_url = "https://tensor.ru/about"
    actual_url = popodrobnee.driver.current_url
    assert actual_url == expected_url
    
#     def test_tensor_page(self):
#         # Открываем сайт https://tensor.ru/
#         self.driver.get('https://tensor.ru/')

#         # Проверяем, что есть блок "Сила в людях"
#         strength_in_people = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.ID, 'strength-in-people')))
#         assert strength_in_people is not None

#         # Переходим в "Подробнее" и проверяем URL
#         details = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.LINK_TEXT, 'Подробнее')))
#         details.click()

#         assert self.driver.current_url == 'https://tensor.ru/about'

#         # Проверяем размеры фотографий в разделе "Работаем"
#         images = self.driver.find_elements(
#             By.XPATH, '//div[@id="work-with-us"]//img')
#         heights = {image.size['height'] for image in images}
#         widths = {image.size['width'] for image in images}
#         assert len(heights) == 1 and len(widths) == 1


if __name__ == '__main__':
    pytest.main()
