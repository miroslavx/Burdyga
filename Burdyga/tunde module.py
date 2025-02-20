from Burdyga import *
a= int(input("sisseta arv1: "))
b= int(input("sisseta arv2: "))
a= input("sisseta arv3: ")
vastus = summa3(a,b, int(c))
print (vastus)


# (1)
def arithmetic(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Деление на ноль"
        else:
            return a / b
    else:
        return "Неизвестная операция"

# (2)
def is_year_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# (3)
def square(side):
    from math import sqrt
    perimeter = 4 * side
    area = side * side
    diagonal = side * sqrt(2)
    return perimeter, area, diagonal

# (4)
def season(month):
    if month in (12, 1, 2):
        return "talv"
    elif month in (3, 4, 5):
        return "kevad"
    elif month in (6, 7, 8):
        return "suvi"
    elif month in (9, 10, 11):
        return "sügis"
    else:
        return "Vale kuu"

# (5)
def bank(a, years):
    for i in range(years):
        a += a * 0.1
    return a

# (6)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# (7)
def date(day, month, year):
    if month < 1 or month > 12 or day < 1:
        return False
    if is_year_leap(year):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > days_in_month[month - 1]:
        return False
    return True

# (8)
def XOR_cipher(s, key):
    result = ""
    for ch in s:
        result += chr(ord(ch) ^ key)
    return result

def XOR_uncipher(s, key):
    result = ""
    for ch in s:
        result += chr(ord(ch) ^ key)
    return result