from .pages.product_page import ProductPage

def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, ProductPage.productTestLink)
    page.open()
    page


