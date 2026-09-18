def month_to_season(num):
    if num in (12, 1, 2):
        return 'Зима'
    if num in (3, 4, 5):
        return 'Весна'
    if num in (6, 7, 8):
        return 'Лето'
    if num in (9, 10, 11):
        return 'Осень'
    else:
        return 'Неверный номер месяца'


print(month_to_season(1))
