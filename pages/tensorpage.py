from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class TensorPage(BasePage):
    def check_sila_v_lyudyah(self):
        sila_block_locator = (By.XPATH, "//h2[text()='Сила в людях']")
        self.assert_element_displayed(sila_block_locator)

    def go_to_about(self):
        podrobnosti_link_locator = (By.LINK_TEXT, "Подробнее")
        self.click_element(podrobnosti_link_locator)
        about_url_locator = (EC.url_to_be, "https://tensor.ru/about")
        self.wait_for_element(about_url_locator)

    def check_work_photos(self):
        photos_locator = (By.XPATH, "//div[@class='work-photos']//img")
        photos = self.driver.find_elements(*photos_locator)
        first_photo_size = photos[0].size
        for photo in photos[1:]:
            assert photo.size == first_photo_size
