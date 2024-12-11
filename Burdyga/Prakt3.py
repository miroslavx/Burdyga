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
