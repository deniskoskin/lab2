import math

a = float(input("Введите числовое значение первого катета: "))
b = float(input("Введите числовое значение второго катета: "))
c = float(input("Введите числовое значение гипотенузы: "))

def func(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        pp = ((a + b + c) / 2)

        sum = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))

        print("Площадь треугольника: ", round(sum, 2))
    else:
        print("Такого треугольника не существует")

func(a,b,c)



