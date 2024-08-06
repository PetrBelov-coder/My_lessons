# В fake_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
# В true_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)
from fake_math import divide as d1
from true_math import divide as d2

first = float(input("Введите первое число :"))
second = float(input("Введите второе число :"))
res = d1(first,second)
print(res)
res = d2(first,second)
print(res)

#from math import inf