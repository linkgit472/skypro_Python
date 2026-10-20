import allure
from page.page_auth import AuthPage
from page.page_shop import ShopPage
from page.page_shopping_cart import ShoppingCartPage
from page.page_form import FormPage


@allure.epic("Магазин")
@allure.feature("Оформление заказа")
@allure.story("Сквозной сценарий покупки набора товаров")
@allure.title("Успешная покупка трех товаров с проверкой итоговой стоимости")
@allure.description(
    "Тест проверяет полный цикл покупки в интернет-магазине. "
    "Происходит авторизация пользователя standard_user, выбор и добавление "
    "трех товаров в корзину, валидация состава корзины, ввод персональных "
    "данных на форме доставки и финальная проверка итоговой стоимости заказа."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(driver):
    auth = AuthPage(driver)
    shop = ShopPage(driver)
    shopping_cart = ShoppingCartPage(driver)
    form = FormPage(driver)

    auth.auth_form('standard_user', 'secret_sauce')
    shop.add_item()
    shopping_cart.check_items(3)
    shopping_cart.checkout_btn()
    form.fill_form("Karina", "Egelman", "215099")

    with allure.step("Проверить, что итоговая сумма заказа содержит '$58.29'"):
        total_price = form.get_total()
        assert '$58.29' in total_price, (
            f"Ошибка: Ожидаемая сумма '$58.29' не найдена. "
            f"Фактический текст на экране: '{total_price}'"
        )
