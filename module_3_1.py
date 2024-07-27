# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
calls = 0

# Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях.
def count_calls():
    global calls
    calls = calls + 1
    return calls

# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
def string_info():
    count_calls()
    string = input("Введите строку : ")
    l_ = len(string)
    string_up = string.upper()
    string_low = string.lower()
    tuple = (l_, string_up, string_low)
    print("string_info(", string, ") :", tuple)
    return tuple

# Создать функцию is_contains с двумя параметрами string и list_, реализовать логику работы по описанию.
def is_contains() :
    count_calls()
    string = input("Введите строку : ")
    list_ = input("Введите список строк : ")
    res = string in list_
    print("res =", res)
    if res == False :
        result = " не содержится "
    if res == True :
        result = " содержится "
    print("Подстрока ",string, result, "в списке строк: ", list_ )
    return res

# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
#string_info()
#string_info()
#string_info()
#is_contains()
is_contains()

# Вывести значение переменной calls на экран(в консоль).
print("Число вызовов: ", calls)





