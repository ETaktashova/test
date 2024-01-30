import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contactpage import ContactsPage, contacts_buttton_locator
# Второй сценарий:
# 1) Перейти на https://sbis.ru/ в раздел "Контакты"
# 2) Проверить, что определился ваш регион (в нашем примере
# Ярославская обл.) и есть список партнеров.
# 3) Изменить регион на Камчатский край
# 4) Проверить, что подставился выбранный регион, список партнеров
# изменился, url и title содержат информацию выбранного региона
driver = webdriver.Chrome()
def test_my_region():
    contacts = ContactsPage(driver)
    contacts.open()
    contacts.find(contacts_buttton_locator).click()
# Закрытие браузера
# driver.quit()

if __name__ == '__main__':
    pytest.main()