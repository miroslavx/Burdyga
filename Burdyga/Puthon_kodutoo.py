# программа демонстрирует разные функции для работы со строками
def main():
    while True:
        print("\n" + "=" * 50)
        print("Valige funktsioon demonstreerimiseks:")
        print("1. Numbrite kontroll (isdigit)")
        print("2. Alamstringi otsimine (find)")
        print("3. Stringi asendamine (replace)")
        print("4. Stringi jagamine (split)")
        print("5. Stringide ühendamine (join)")
        print("6. Registri muutmine (swapcase)")
        print("7. Teksti tsentreerimine (center)")
        print("8. Tühikute eemaldamine (strip)")
        print("9. Esinemiste loendamine (count)")
        print("10. Nullidega täitmine (zfill)")
        print("0. Välju")
        
        choice = input("\nSisestage funktsiooni number (0-10): ")
        
        if choice == "0":
            print("Head aega!")
            break
            
        elif choice == "1":
            # можно проверить состоит ли строка тока из цифр
            text = input("Sisestage tekst kontrollimiseks: ")
            result = text.isdigit()
            print(f"String '{text}' {'' if result else 'ei '}koosneb ainult numbritest")
            
        elif choice == "2":
            # ищем где находится определенное слово/буква в строке
            text = input("Sisestage tekst: ")
            search = input("Mida otsime?: ")
            pos = text.find(search)
            if pos != -1:
                print(f"Leitud positsioonil: {pos}")
            else:
                print("Midagi ei leitud :(")
            
        elif choice == "3":
            # заменяем в строке одно на другое
            text = input("Sisestage tekst: ")
            old = input("Mida asendame: ")
            new = input("Millega asendame: ")
            result = text.replace(old, new)
            print(f"Tulemus: {result}")
            
        elif choice == "4":
            # разбиваем строку на части по разделителю
            text = input("Sisestage tekst tühikutega: ")
            words = text.split()
            print("Saadud sõnad:")
            for i, word in enumerate(words, 1):
                print(f"{i}. {word}")
            
        elif choice == "5":
            # склеиваем несколько строк в одну
            words = input("Sisestage sõnad tühikutega: ").split()
            separator = input("Sisestage eraldaja: ")
            result = separator.join(words)
            print(f"Tulemus: {result}")
            
        elif choice == "6":
            # заменяем регистр букв на противоположный
            text = input("Sisestage tekst registri muutmiseks: ")
            result = text.swapcase()
            print(f"Tulemus: {result}")
            
        elif choice == "7":
            # выравниваем текст по центру
            text = input("Sisestage tekst: ")
            width = int(input("Sisestage kogupikkus: "))
            result = text.center(width, '*')
            print(f"Tulemus:\n{result}")
            
        elif choice == "8":
            # убираем лишние пробелы в начале и конце алгоритма
            text = input("Sisestage tekst tühikutega:   ")
            result = text.strip()
            print(f"Pikkus enne töötlemist: {len(text)}")
            print(f"Pikkus pärast töötlemist: {len(result)}")
            print(f"Tulemus: '{result}'")
            
        elif choice == "9":
            # щитаем сколько раз встречается символ/строка
            text = input("Sisestage tekst: ")
            search = input("Mida loendada?: ")
            count = text.count(search)
            print(f"Esineb {count} korda")
            
        elif choice == "10":
            # добавляем нули слева до нужной длины
            number = input("Sisestage number: ")
            width = int(input("Sisestage soovitud pikkus: "))
            result = number.zfill(width)
            print(f"Tulemus: {result}")
            
        else:
            print("Vale valik! Proovige uuesti.")
        
        input("\nVajutage jätkamiseks Enter...")

if __name__ == "__main__":
    main()