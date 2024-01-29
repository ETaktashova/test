import pytest
from selenium import webdriver
from contactpage import ContactsPage
from tensorpage import TensorPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_scenario(setup):
    driver = setup
    contacts_page = ContactsPage(driver)
    contacts_page.go_to_tensor()

    tensor_page = TensorPage(driver)
    tensor_page.check_sila_v_lyudyah()
    tensor_page.go_to_about()
    tensor_page.check_work_photos()
