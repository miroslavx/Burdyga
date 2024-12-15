# Программа для проверки знаний по математике

print("Добро пожаловать в программу проверки знаний по математике!")

# Выбор уровня сложности
print("Выберите уровень сложности:")
print("1. Tase 1")
print("2. Tase 2")
print("3. Tase 3")

while True:
    level = input("Введите номер уровня (1, 2 или 3): ")
    if level in ['1', '2', '3']:
        level = int(level)
        break
    else:
        print("Пожалуйста, введите 1, 2 или 3.")

# Настройки в зависимости от уровня
if level == 1:
    operations = ['+', '-']
    max_num = 10
    num_operations = 1
elif level == 2:
    operations = ['+', '-', '*']
    max_num = 50
    num_operations = 2
else:
    operations = ['+', '-', '*', '/']
    max_num = 100
    num_operations = 3

# Выбор количества примеров
while True:
    total = input("Сколько примеров вы хотите решить? Введите число: ")
    if total.isdigit() and int(total) > 0:
        total = int(total)
        break
    else:
        print("Пожалуйста, введите положительное число.")

correct = 0

# Простейший генератор "случайных" чисел
seed = 1

for i in range(total):
    # Генерация "случайных" чисел и операторов
    num1 = seed % max_num + 1
    op1 = operations[seed % len(operations)]
    seed = (seed * 3 + 7) % 100
    if num_operations == 1:
        expression = f"{num1} {op1} {seed % max_num + 1}"
    elif num_operations == 2:
        num2 = seed % max_num + 1
        op2 = operations[seed % len(operations)]
        seed = (seed * 3 + 7) % 100
        expression = f"{num1} {op1} {num2} {op2} {seed % max_num + 1}"
    else:
        num2 = seed % max_num + 1
        op2 = operations[seed % len(operations)]
        seed = (seed * 3 + 7) % 100
        num3 = seed % max_num + 1
        op3 = operations[seed % len(operations)]
        seed = (seed * 3 + 7) % 100
        expression = f"{num1} {op1} {num2} {op2} {num3} {op3} {seed % max_num + 1}"

    # Избегаем деления на ноль
    if '/' in expression:
        parts = expression.split()
        for j in range(len(parts)):
            if parts[j] == '/':
                if int(parts[j+1]) == 0:
                    parts[j+1] = '1'  # Заменяем 0 на 1
        expression = ' '.join(parts)

    # Вычисление результата
    try:
        result = eval(expression)
        if '/' in expression:
            result = round(result, 2)
    except:
        result = "Ошибка"

    # Вывод примера и получение ответа
    print(f"Пример {i+1}: {expression} = ?")
    answer = input("Ваш ответ: ")

    # Проверка ответа
    try:
        if float(answer) == result:
            print("Правильно!\n")
            correct += 1
        else:
            print(f"Неправильно. Правильный ответ: {result}\n")
    except:
        print(f"Неправильно. Правильный ответ: {result}\n")

# Вычисление процента правильных ответов
percent = (correct / total) * 100

# Определение оценки
if percent < 60:
    grade = "Hinne 2"
elif percent < 75:
    grade = "Hinne 3"
elif percent < 90:
    grade = "Hinne 4"
else:
    grade = "Hinne 5"

# Вывод результата
print(f"Вы решили {correct} из {total} примеров правильно.")
print(f"Ваш результат: {percent:.2f}% - {grade}")