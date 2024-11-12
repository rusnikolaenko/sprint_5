from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls
from data.data import PersonData


class TestUserAuthentication:

    def test_successful_login_redirects_to_main(self, login):
        """Check that successful login redirects to the main page."""
        driver = login

        order_btn = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_btn.text == 'Оформить заказ'

    def test_login_via_account_button(self, driver):
        """Test login via the 'Войти в аккаунт' button."""
        driver.find_element(*MainPage.mn_auth).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_btn = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_btn.text == 'Оформить заказ'

    def test_login_via_profile_button(self, driver):
        """Test login via the 'Личный Кабинет' button."""
        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_btn = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_btn.text == 'Оформить заказ'

    def test_login_from_registration_form(self, driver):
        """Test login via the 'Войти' link on the registration form."""
        driver.get(Urls.url_register)

        driver.find_element(*AuthLogin.al_login_text_with_href).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_btn = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_btn.text == 'Оформить заказ'

    def test_login_from_password_recovery_form(self, driver):
        """Test login via the 'Войти' link on the password recovery form."""
        driver.get(Urls.url_forgot_password)

        driver.find_element(*AuthPassword.ap_login_text_with_href).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_btn = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_btn.text == 'Оформить заказ'
