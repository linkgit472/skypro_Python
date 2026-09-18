from page.page_auth import AuthPage
from page.page_shop import ShopPage
from page.page_shopping_cart import ShoppingCartPage
from page.page_form import FormPage


def test_shop_total(driver):
    auth = AuthPage(driver)
    shop = ShopPage(driver)
    shopping_cart = ShoppingCartPage(driver)
    form = FormPage(driver)

    auth.auth_form('standard_user', 'secret_sauce')
    shop.add_item()
    shopping_cart.check_item()
    shopping_cart.checkout_btn()
    form.fill_form("Karina", "Egelman", "215099")
    assert '$58.29' in form.get_total()
