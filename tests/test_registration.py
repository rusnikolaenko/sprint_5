import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData


class TestUserRegistration:

    def test_successful_registration_redirects_to_login(self, driver):
        """Upon successful registration, the user is redirected to the login page."""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_element_with_login_text))

        login_header = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login and login_header.text == 'Вход'

    def test_registration_with_empty_name_field(self, driver):
        """Test that registration does nothing when the name field is empty."""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_email_field).send_keys('test1@yan.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('124567')

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AuthRegistre.ar_register_button))
        time.sleep(2)
        error_messages = driver.find_elements(*AuthRegistre.ar_error_message)

        assert driver.current_url == Urls.url_register and len(error_messages) == 0

    @pytest.mark.parametrize('invalid_email', [
        'test1@yanru', 'test2yan.ru', 'te st3@yan.ru', 'test4@ya n.ru',
        '@yan.ru', 'test6@.ru', 'test7@yan.'
    ])
    def test_registration_with_invalid_email(self, driver, invalid_email):
        """Test that an error is shown when using an invalid email."""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Test User')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(invalid_email)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('123456')

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistre.ar_error_message_2))
        error_msg = driver.find_element(*AuthRegistre.ar_error_message_2)

        assert error_msg.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('short_password', ['1', '12345'])
    def test_registration_with_short_password(self, driver, short_password):
        """Test that an error is shown when the password is too short."""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Test User')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('test1@yan.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(short_password)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistre.ar_error_message))
        error_msg = driver.find_element(*AuthRegistre.ar_error_message)

        assert error_msg.text == 'Некорректный пароль'
