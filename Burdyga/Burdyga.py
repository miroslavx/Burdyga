print("Tere tulemast matemaatika teadmiste testimise programmi!")

print("Valige raskusaste:")
print("1. Tase 1")
print("2. Tase 2")
print("3. Tase 3")

while True:
    level = input("Sisestage taseme number (1, 2 või 3): ")
    if level in ['1', '2', '3']:
        level = int(level)
        break
    else:
        print("Palun sisestage 1, 2 või 3.")

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

while True:
    total = input("Mitu ülesannet soovite lahendada? Sisestage arv: ")
    if total.isdigit() and int(total) > 0:
        total = int(total)
        break
    else:
        print("Palun sisestage positiivne arv.")

correct = 0
seed = 1

for i in range(total):
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

    if '/' in expression:
        parts = expression.split()
        for j in range(len(parts)):
            if parts[j] == '/':
                if int(parts[j+1]) == 0:
                    parts[j+1] = '1'
        expression = ' '.join(parts)

    try:
        result = eval(expression)
        if '/' in expression:
            result = round(result, 2)
    except:
        result = "Viga"

    print(f"Ülesanne {i+1}: {expression} = ?")
    answer = input("Teie vastus: ")

    try:
        if float(answer) == result:
            print("Õige!\n")
            correct += 1
        else:
            print(f"Vale. Õige vastus: {result}\n")
    except:
        print(f"Vale. Õige vastus: {result}\n")

percent = (correct / total) * 100

if percent < 60:
    grade = "Hinne 2"
elif percent < 75:
    grade = "Hinne 3"
elif percent < 90:
    grade = "Hinne 4"
else:
    grade = "Hinne 5"

print(f"Lahendasite õigesti {correct} ülesannet {total}-st.")
print(f"Teie tulemus: {percent:.2f}% - {grade}")
