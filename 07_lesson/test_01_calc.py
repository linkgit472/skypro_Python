from page.page_calc import CalcPage


def test_calc(driver):
    calc = CalcPage(driver)
    calc.delay_field(45)
    calc.sum_7_8()

    assert calc.get_result() == '15'
