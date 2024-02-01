from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contactpage import ContactsPage
driver = webdriver.Chrome()
open_download_page_locator = (
    By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[10]/ul/li[6]/a'
)
plugin_locator = (
    By.XPATH, "//div[contains(@class, 'controls-TabButton__caption') and text()='СБИС Плагин']")
download_link_locator = (
    By.XPATH, '//a[@class="sbis_ru-DownloadNew-loadLink__link js-link"]')


def test_download_file():
    sbis = ContactsPage(driver)
    sbis.open()
    button_page_downl = sbis.find(
        open_download_page_locator)
    # перекрытый элемент
    driver.execute_script("arguments[0].scrollIntoView();", button_page_downl)
    button_page_downl.click()
    window_after = driver.window_handles[-1]
    sbis.driver.switch_to.window(window_after)
    plugin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(plugin_locator))
    # JavaScript для удаления или скрытия перекрывающего элемента перед кликом
    driver.execute_script(
        "var overlay = document.querySelector('.controls-tabButton__overlay'); if (overlay) overlay.style.display = 'none';")
    actions = ActionChains(driver)
    actions.move_to_element(plugin_button).click().perform()
    driver.execute_script(
        "var overlay = document.querySelector('.controls-tabButton__overlay'); if (overlay) overlay.style.display = 'none';")
    plugin_button.click()

    # download_link_button = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located(download_link_locator))
    # download_link_button.is_displayed()
    # download_link_button.click()
    # assert driver.current_url == 'https://sbis.ru/download?tab=plugin&innerTab=default'


    # WebDriverWait(driver, 5)
# Закрытие браузера
# driver.quit()
if __name__ == '__main__':
    pytest.main()
