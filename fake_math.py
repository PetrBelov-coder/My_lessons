# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
def divide(first, second) :
    if second == 0 and first == 0 :
        print("Неопределенность по Лопиталю: res = ",first,"/",second  )
        return
    elif second == 0 and first != 0 :
        print("Ошибка деления на ноль : res = ",first,"/",second )
        return
    else :
        res = first / second
    return res


