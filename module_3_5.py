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
                str_number_without_null = str_number_without_null + i
        l_ = len(str_number_without_null)
        if l_ == 1 :
            first = int(str_number_without_null[0])
        if l_ > 1 :
            first = int(str_number_without_null[0])
            multiplaer = get_multiplied_digits(int(str_number_without_null[1:]))
            result = first * multiplaer
        else :
            result = int(str_number_without_null)
    return result

number = int(input("Введите целое число : "))
result = get_multiplied_digits(number)
print("Произведение значащих цифр в числе ", number, " равно ", result)
