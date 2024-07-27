# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True),
# которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a , b , c ) :
    print("Актуальный тип параметра a: ", a, type(a))
    print("Актуальный тип параметра b: ", b, type(b))
    print("Актуальный тип параметра c: ", c, type(c))
    print(a,b,c)

# Функция должна выводить эти параметры.
print_params(25,"string" , False)

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(1, 25 , True) # line 11, in <module> print_params(b = 25)
print_params(1, "строка", c = [1,2,3]) # TypeError: print_params() missing 2 required positional arguments

# 2.Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
values_list = [12345, "12345", {1 :12345}]
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params разных типов.
values_dict = { "a" : 12345, "b" : "12345", "c" : [12345]}
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров.
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [123, "123"]
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)