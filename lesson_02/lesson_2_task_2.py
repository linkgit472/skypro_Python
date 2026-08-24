def is_year_leap(num):
    return num % 4 == 0


year = int(input('Введите номер года: '))
result = is_year_leap(year)

print(f"год {year}: {result}")
