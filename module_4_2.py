# Домашнее задание по уроку "Пространство имен"
#
# Ваша задача:
# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function,
# функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function() :
    def inner_function() :
        print("Я в области видимости функции test_function")
        return
    inner_function()
    print("Я вне области видимости функции inner_function")
    return

test_function()

