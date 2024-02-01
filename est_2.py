import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contactpage import *

driver = webdriver.Chrome()
# проверка установления моего региона и списка партнеров по нему
def test_my_region():
    contacts = ContactsPage(driver)
    contacts.open()
    contacts.find(contacts_buttton_locator).click()

    my_region = contacts.wait_for_element(my_region_locator)
    partners_my_reg_list = contacts.wait_for_element(partners_locator_my_reg)
    assert partners_my_reg_list.is_displayed(
    ), 'Список партнеров не отображается на странице'
    assert my_region.text == 'Тюменская обл.', 'Мой регион устанавливается неверно'


def test_kamchat_reg():
    contacts = ContactsPage(driver)
    contacts.open()
    contacts.find(contacts_buttton_locator).click()
    my_region = contacts.find(my_region_locator)
    my_region.click()
    # меняем регион - переходим на камчатку
    select_kamchat_reg = contacts.wait_for_element(locator_kamchat_reg_inregions_list)
    select_kamchat_reg.click()
    WebDriverWait(driver, 5).until(EC.url_contains('kamchatskij-kraj'))
    new_url = driver.current_url
    kamchatka_reg_is_displayed = contacts.find(kamchatka_locator)
    title_kamchatka = kamchatka_reg_is_displayed.get_attribute('title')
    # проверка урла и тайтл
    assert 'kamchatskij-kraj' in new_url
    assert title_kamchatka in kamchatka_reg_is_displayed.get_attribute(
        "title"), "Атрибут title не содержит информацию о выбранном регионе"
    # проверяем, что подставился выбранный регион, список партнеров(и он изменился)
    assert kamchatka_reg_is_displayed.text == 'Камчатский край'
    # Сравниваем содержимое каждого элемента в списках партнеров
    kamchatka_partners = driver.find_elements(
        By.XPATH, "//div[@class='controls-ListViewV__itemsContainer']//div[@class='controls-ListView__itemV-relative']")
    tyumen_partners = driver.find_elements(
        By.XPATH, "//div[@class='controls-ListViewV__itemsContainer']//div[@class='controls-ListView__itemV-relative']")
    for kamchatka_partner, tyumen_partner in zip(kamchatka_partners, tyumen_partners):
        assert kamchatka_partner.text != tyumen_partner.text, "Содержимое партнеров в разных регионах совпадает"


# Закрытие браузера
# driver.quit()
if __name__ == '__main__':
    pytest.main()
