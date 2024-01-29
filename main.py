from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
driver = webdriver.Chrome()
driver.get('https://sbis.ru/')
cont_but = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Контакты'))
)
cont_but.click()


driver.switch_to.window(driver.window_handles[-1])

tensor_but = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')))
tensor_but.click()
