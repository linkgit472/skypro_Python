# Тест 2. Заполнение формы
# Цель: написать автотест для проверки функциональности заполнения формы
# на сайте https://bonigarcia.dev/, используя паттерн Page Object.

# Шаги
# Создать класс для страницы с формой, который будет содержать методы
# для взаимодействия с элементами формы (поля ввода, кнопка Submit)
# и проверки состояния полей (подсветка цветом).
# Написать тест, который использует Page Object для заполнения формы данными:
# First name: Иван
# Last name: Петров
# Address: Ленина, 55/3
# Email: test@skypro.com
# Phone number: +7985899998787
# Zip code: оставить пустым
# City: Москва
# Country: Россия
# Job position: QA
# Company: Skypro
# Нажать кнопку Submit.
# Проверить (assert), что поле Zip code подсвечено красным.
# Проверить (assert), что остальные поля подсвечены зеленым.


from page_form import FormPage


def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()
