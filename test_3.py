from time import sleep
import pytest
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contactpage import ContactsPage
from locators import (
    open_download_page_locator,
    plugin_locator,
    download_link_locator
)
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory":  f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option('prefs', prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


def test_download_file():

    sbis = ContactsPage(driver)
    sbis.open()
    button_page_downl = sbis.find(
        open_download_page_locator)
    # перекрытый элемент
    driver.execute_script("arguments[0].scrollIntoView();", button_page_downl)
    sleep(5)
    button_page_downl.click()
    window_after = driver.window_handles[-1]
    sbis.driver.switch_to.window(window_after)
    plugin_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(plugin_locator))
    actions = ActionChains(driver)
    actions.move_to_element(plugin_button).click().perform()
    sleep(5)
    download_link = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located(download_link_locator))
    driver.execute_script("arguments[0].click();", download_link)
    # actions.move_to_element(download_link).click().perform()
    # download_link.click()

    download_directory = f"{os.getcwd()}/downloads"
    # пока проверяется наличие зотя бы одного нового файла в папке
    files = os.listdir(download_directory)
    assert len(files) > 0, "Нет файлов в папке загрузок"
    # file_size = os.path.getsize(download_directory)
    # assert file_size == 7.02


# Закрытие браузера
# driver.quit()
if __name__ == '__main__':
    pytest.main()
