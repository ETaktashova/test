from selenium.webdriver.common.by import By


contacts_buttton_locator = (By.LINK_TEXT, 'Контакты')
my_region_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
kamchatka_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
partners_locator_my_reg = (
    By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
partners_locator_kamchat_list = (
    By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
locator_kamchat_reg_inregions_list = (
    By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')

tensor_button_locator = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')
block_sila_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
popodrobnee_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
section_rabotaem_locator = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[4]')
open_download_page_locator = (
    By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[10]/ul/li[6]/a'
)
plugin_locator = (
    By.XPATH, "//div[contains(@class, 'controls-TabButton__caption') and text()='СБИС Плагин']")
download_link_locator = (
    By.XPATH, '//a[@class="sbis_ru-DownloadNew-loadLink__link js-link"]')