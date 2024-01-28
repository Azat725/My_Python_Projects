year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0:
    print("Год висакосный")
elif year % 400 == 0:
    print("Год висакосный")
else:
    print("Год не является високосным")