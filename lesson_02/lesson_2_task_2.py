def is_year_leap(num):
    return True if num % 4 == 0 else False


year = 2023
result = is_year_leap(year)
print(f'год {year}: {result}')
