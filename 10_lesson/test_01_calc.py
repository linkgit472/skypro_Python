import allure
from page.page_calc import CalcPage


@allure.epic("Калькулятор")
@allure.feature("Математические операции")
@allure.story("Сложение чисел с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения чисел 7 и 8 с учетом задержки")
@allure.description(
    "Тест проверяет корректность работы медленного калькулятора. "
    "Устанавливается задержка в 45 секунд, выполняется сложение 7 + 8 "
    "и проверяется, что итоговый результат равен 15."
)
def test_calc(driver):
    calc = CalcPage(driver)
    calc.delay_field(45)
    calc.sum_7_8()

    with allure.step("Проверить, что итоговое значение на экране равно '15'"):
        actual_result = calc.get_result()
        assert actual_result == '15', ("Ожидали '15', "
                                       f"а получили '{actual_result}'")
