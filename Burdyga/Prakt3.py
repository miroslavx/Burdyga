#ül 15
for _ in range(10):
    print("0 1 2 3 4 5 6 7 8 9")

#ül14
N = int(input("Sisesta N: "))
result = 1
for num in range(1, N + 1):
    result *= num
print("Korrutis:", result)

#ül13
count = 0
total = 0
for num in range(100, 1001):
    if num % 7 == 0:
        count += 1
        total += num
print("Arvude arv:", count)
print("Arvude summa:", total)

#ül12
N = int(input("Muruniidukite arv: "))
m = int(input("Esimese muruniiduki tunnid: "))
total_hours = 0
for i in range(N):
    total_hours += m + i / 6  
print("Kokku tunde:", total_hours)

#Ül11
import random

k = random.randint(1, 10)
result = 1
for num in range(10, 100):
    if num % 2 != 0 and num % k == 0:
        result *= num
print("Korrutis:", result)

#ÜL10
for _ in range(10):
    a, b = map(int, input("Sisesta kaks arvu tühikuga eraldatult: ").split())
    print("Suurem arv:", max(a, b))

#ül9
S = float(input("Sisesta hoiuse summa: "))
N = int(input("Sisesta aastate arv: "))
for _ in range(N):
    S *= 1.03

print(f"Summa pärast {N} aastat: {round(S, 2)}")

#Ül8
for inches in range(1, 21):
    print(f"{inches} tolli = {inches * 2.5} cm")
#Ül7

A = int(input("Sisesta vahemiku algus A: "))

B = int(input("Sisesta vahemiku lõpp B: "))
K = int(input("Sisesta arv K: "))
for num in range(A, B + 1):
    if num % K == 0:
        print(num)

#Ül6
N = int(input("Sisesta arvude arv: "))
positive, negative, zeros = 0, 0, 0
for _ in range(N):
    num = int(input("Sisesta arv: "))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1
print("Positiivsed:", positive, "Negatiivsed:", negative, "Nullid:", zeros)
  
  #ül5
N = int(input("Sisesta arvude arv: "))
total = 0
for _ in range(N):
    num = int(input("Sisesta arv: "))
    if num < 0:
        total += num
print("Negatiivsete arvude summa:", total)

    
    #Ül1

count = 0
for _ in range(15):
    num = float(input("Sisesta arv: "))
    if num.is_integer():
        count += 1
print("Täisarvude arv:", count)


#Ül3
p=1

for j in range(8):
    while True:
        try:
            arv=float(input(f"Sisesta {j+1} arv:"))
            break
        except:
            print("On vaja arv")
if arv>0:
    p*=arv
else:
    print("Korrutame ar")
print(f"{j+1}. samm korrutis= {p}")
print(f"Lõpptulemus on {p}")

#Ül2
while True:
    try:
        A=int(input("Sisseta A:"))
        break
    except:
        print ("On vaja naturaalne arv")
summa=0
if A>0:
    for i in range(1,A+1,1):
        summa=+1
        print(f"i, samm,summa={summa}")
print (f"Vastus {summa} ")

#Ül4
for num in range(10, 21):
    print(num**2)

    #Ül16
    for i in range(1, 10):
        row = ["0"] * 9
        row[i - 1] = str(i)
    print(" ".join(row))

