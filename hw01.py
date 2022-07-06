__author__ = 'Сидоров Артур Николаевич'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...
#age = int(input("Enter your age:"))
#name = input("Enter your name:")
age = 25
name = "Arthur"
dif = age - 18
if dif > 0:
    print(name, "на", dif, "года/лет больше 18\n")
elif dif < 0:
    dif = -dif
    print(name, "на", dif, "года/лет меньше 18\n")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...
first = int (input("Enter the first value: "))
second = int (input("Enter the second one: "))
print('A variable "first" stores', first, 'and variable "second" stores', second)
tmp = first
first = second
second = tmp
print('Values are swaped. The variable "first" stores', first, "whereas", second, 'is in "second"')
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...
import math
a = int(input('Enter "a":'))
b = int(input('Enter "b":'))
c = int(input('Enter "c":'))
discrim = (b**2) - 4 *a * c
if discrim == 0:
    print("Equation has only one root:", -b / (2 * a))
elif discrim < 0:
    print("Equation has no roots")
else:
    print("x1 =", (-b + math.sqrt(discrim))/(2 * a), "x2 =", (-b - math.sqrt(discrim))/(2 * a))
