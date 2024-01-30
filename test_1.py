import pytest
from pages.tensorpage import TensorPage, tensor_button_locator, block_sila_locator, popodrobnee_locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contactpage import ContactsPage, contacts_buttton_locator
image_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]')
driver = webdriver.Chrome()
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

# def test_url_tensor_about():
#     popodrobnee_page = TensorPage(driver)
#     popodrobnee_page.open()
#     # скроем элемент, пока другие его перекрывают
#     driver.execute_script(
#         "arguments[0].style.display = 'none';", driver.find_element(By.XPATH, '//noindex'))

#     popodr_button = driver.find_element(*popodrobnee_locator)
#     # прибегнула к исп-нию JavaScript-кода, другого способа пока не нашла
#     driver.execute_script("arguments[0].click();", popodr_button)
#     expected_url = "https://tensor.ru/about"
#     actual_url = driver.current_url
#     assert actual_url == expected_url


def test_image_size():
    pass


# Закрытие браузера
driver.quit()

if __name__ == '__main__':

    pytest.main()
