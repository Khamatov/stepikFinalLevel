from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):
    productTestLink = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    def