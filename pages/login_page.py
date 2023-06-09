from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    loginPageLink = 'http://selenium1py.pythonanywhere.com'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'the login-form is not on this page'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM), 'the registration-form is not on this page'
