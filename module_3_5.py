# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
#
# Пункты задачи:
# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number) :
    if type(number) != int :
        print("Параметр ", number, " не является целым числом")
    else :
        str_number = str(number)
        str_number_without_null = ""
        for i in str_number :
            if i != "0" :
                str_number_without_null += i
        l_ = len(str_number_without_null)
        first = int(str_number_without_null[0])
        if l_ > 1 :
            result = first * get_multiplied_digits(int(str_number_without_null[1:]))
        else :
            result = first
        print("Произведение значащих цифр в числе ", number, " равно ", result)
    return

get_multiplied_digits(304010)

# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получится взять срез str_number[1:].
# Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.