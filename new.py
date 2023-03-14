#Задание 1
a = 10
b = 5
print(a + b)
#1.1
a = input("Оценка?")
print(a)
#Задание 2
time = int(input("Ввод времени в секундах"))
a = time // 3600
b = (time - a * 3600) // 60
c = (time - a * 3600) - b * 60
print (a , b , c)
#Задание 3
a = int(input("Введите число"))
s = str(a)
b = s
c = s + s
d = s + s + s
print(int(b) + int(c) + int(d))
#Задание 4
a = int(input("Ввод числа"))
max = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max:
        max = a % 10
    if a > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
print(a)
#Задание 5
a = float(input("Значение выручки"))
b = float(input("Значение издержек фирмы"))
if a > b:
    print(f"Прибыль.Рентабельность {a / b}")
    n = int(input("Ввести численность сотрудников"))
    print(f"Прибыль фирмы в расчете на одного сотрудника {a / n}")
else:
    print("Убыток")
#Задание 6
a = int(input("Ввод результатов первого дня"))
b = int(input("Ввод конечного результата"))
c = 1
while a < b:
    a = a + a * 0.1
    c +=1
    print(c)


