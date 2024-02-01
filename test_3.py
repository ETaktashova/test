from time import sleep
import pytest, os
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
    plugin_locator
) 
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory" :  f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option('prefs', prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


download_link_locator = (
    By.XPATH, '//a[@class="sbis_ru-DownloadNew-loadLink__link js-link"]')


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
        EC.element_to_be_clickable(plugin_locator))
    # JavaScript для удаления или скрытия перекрывающего элемента перед кликом
    actions = ActionChains(driver)
    actions.move_to_element(plugin_button).click().perform()
    driver.execute_script(
        "var overlay = document.querySelector('.controls-tabButton__overlay'); if (overlay) overlay.style.display = 'none';")
    sleep(10)
    plugin_button.click()

    # download_link_button = driver.find_elements('xpath', '//a')[1]
    # download_link_button.click()



    # WebDriverWait(driver, 5)
# Закрытие браузера
# driver.quit()
if __name__ == '__main__':
    pytest.main()
