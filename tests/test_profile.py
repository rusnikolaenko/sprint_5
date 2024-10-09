from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls


class TestUserProfile:

    def test_open_profile_page(self, login):
        """Verify that the profile page opens when clicking the profile button."""
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        history_button = driver.find_element(*LKProfile.lk_history_shop_button)
        assert driver.current_url == Urls.url_profile and history_button.text == 'История заказов'

    def test_switch_to_constructor_via_button(self, login):
        """Test navigation to the constructor from the profile via the 'Конструктор' button."""
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        driver.find_element(*MainPage.mn_constructor_button).click()

        header_elements = driver.find_elements(By.XPATH, ".//h1")
        assert len(header_elements) > 0 and header_elements[0].text == 'Соберите бургер'

    def test_switch_to_constructor_via_logo(self, login):
        """Test navigation to the constructor from the profile by clicking the logo."""
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        driver.find_element(*MainPage.mn_logo).click()

        header_elements = driver.find_elements(By.XPATH, ".//h1")
        assert len(header_elements) > 0 and header_elements[0].text == 'Соберите бургер'

    def test_logout_from_profile_page(self, login):
        """Verify that logging out from the profile page works correctly."""
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LKProfile.lk_info_message))

        driver.find_element(*LKProfile.lk_logout_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_button_any_forms))

        login_header = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login and login_header.text == 'Вход'
