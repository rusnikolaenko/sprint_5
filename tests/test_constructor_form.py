from web_locators.locators import *


class TestBurgerConstructor:

    def test_navigate_to_sauces_section(self, login):
        """Ensure navigation to 'Соусы' section works properly."""
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_sauces_button).click()

        sauce_header = driver.find_element(*MainPage.mn_h_sauces)

        assert sauce_header.text == 'Соусы'

    def test_navigate_to_fillings_section(self, login):
        """Ensure navigation to 'Начинки' section works properly."""
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        fillings_header = driver.find_element(*MainPage.mn_h_filling)

        assert fillings_header.text == 'Начинки'

    def test_navigate_to_buns_section(self, login):
        """Ensure navigation to 'Булки' section works properly."""
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        driver.find_element(*MainPage.mn_ban_button).click()

        buns_header = driver.find_element(*MainPage.mn_h_ban)

        assert buns_header.text == 'Булки'
