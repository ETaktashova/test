import pytest
from pages.tensorpage import (
    TensorPage,
    tensor_button_locator,
    block_sila_locator, 
    popodrobnee_locator, 
    section_rabotaem_locator
)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contactpage import ContactsPage, contacts_buttton_locator
driver = webdriver.Chrome()

# Проверяю переход на tensor.ru через контакты и  баннер "тензор"
def test_tensor_banner():
    contacts = ContactsPage(driver)
    contacts.open()
    WebDriverWait(contacts.driver, 10).until(EC.element_to_be_clickable(contacts_buttton_locator)).click()
    WebDriverWait(contacts.driver, 10).until(EC.element_to_be_clickable(tensor_button_locator)).click()
    WebDriverWait(contacts.driver, 10).until(EC.number_of_windows_to_be(2))
    # Получаем список идентификаторов вкладок
    window_handles = contacts.driver.window_handles
    # Переключаемся на последнюю открытую вкладку
    contacts.driver.switch_to.window(window_handles[-1])
    expected_url = "https://tensor.ru/"
    actual_url = contacts.driver.current_url
    assert actual_url == expected_url

# Проверить, что есть блок "Сила в людях"
def test_strength_in_people():
    sila = TensorPage(driver)
    sila.open()
    sila.wait_for_element(block_sila_locator)
    assert sila.find(block_sila_locator), "Блок 'Сила в людях' не найден на странице"

def test_url_tensor_about():
    popodrobnee_page = TensorPage(driver)
    popodrobnee_page.open()
    # скроем элемент, пока другие его перекрывают
    driver.execute_script(
        "arguments[0].style.display = 'none';", driver.find_element(By.XPATH, '//noindex'))

    popodr_button = driver.find_element(*popodrobnee_locator)
    # прибегнула к исп-нию JavaScript-кода, другого способа пока не нашла
    driver.execute_script("arguments[0].click();", popodr_button)
    expected_url = "https://tensor.ru/about"
    actual_url = driver.current_url
    assert actual_url == expected_url

# проверка равности размера изображений в блоке Работаем
def test_image_size():
    page = TensorPage(driver)
    page.open("https://tensor.ru/about")   
    # раздел "Работаем"
    section = page.find(section_rabotaem_locator)
    images = section.find_elements(By.TAG_NAME, "img")
    first_image_size = images[0].size
    # к слову, {'height': 287, 'width': 403}
    for image in images:
        assert image.size == first_image_size, f"Размер {image} отличается от остальных в блоке!"

# Закрытие браузера
# driver.quit()

if __name__ == '__main__':
    pytest.main()
