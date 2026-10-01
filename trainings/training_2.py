# employee_list = ["John Snow", "Piter Pen", "Drakula",
# "IvanIV", "Moana", "Juilet"]
# print(employee_list[1] + ', ' + employee_list[-2])


# def dev_by_three(x):
#    return 'Да' if x % 3 == 0 else 'Нет'

# num = int(input('Введите число: '))
# result = dev_by_three(num)
# print(f"Делится ли на три число {num}? - {result}")


# import math

# def min_boxes(x):
#    return math.ceil(x / 5)

# items = int(input('Введите количество предметов: '))
# result = min_boxes(items)
# print(f'Минимальное количество коробок - {result}')


# def check_divisibility(n):
#     for i in range(1, n+1):
#         if (i % 2 == 0) and (i % 4 > 0):
#             print(f'{i} - Делится на 2, но не на 4')
#         elif (i % 2 == 0) and (i % 4 == 0):
#             print(f"{i} - Делится и на 2, и на 4")
#         else: print(i)

# num = int(input('Введите число: '))
# check_divisibility(num)


# def quarter_of_year(month):
#     if 1 <= month <= 3:
#         return "I квартал"
#     if 4 <= month <= 6:
#         return "II квартал"
#     if 7 <= month <= 9:
#         return "III квартал"
#     if 10 <= month <= 12:
#         return "IV квартал"
#     return "Неверный номер месяца"

# month = int(input("Введите номер месяца (1-12): "))
# print(quarter_of_year(month))


# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

# for i in lst:
#     if (i > 15) and (i % 3 == 0):
#         print(i)


# list = list(range(25, 4, -5))
# print(list)


# var_1 = 50
# var_2 = 5

# temp = var_1
# var_1 = var_2
# var_2 = temp
# print(var_1, var_2)
