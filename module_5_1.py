# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.

class House :
    def __init__(self, name, number_of_floors, new_floor) :
        self.name = name
        self.number_of_floors = number_of_floors
        # self.go_to(new_floor)
        def  go_to(new_floor) :
            if new_floor < 1 or new_floor > int(number_of_floors) :
                print("Такого этажа не существует")
            else :
                while i in range(1,self.new_floor) :
                    print("Пройден ", i, "этаж")

h1 = House("ЖК-1", 5, new_floor = 1)
h2 = House("ЖК-2", 7, new_floor = 1)
h3 = House("ЖК-3", 11, new_floor = 1)

name = input("Введите имя интересующего Вас жилого комплекса : ", )
if name == "ЖК-1" :
    new_floor = int(input("Какой этаж желаете осмотреть? ", ))
    h1.go_to(new_floor)
elif name == "ЖК-2" :
    new_floor = int(input("Какой этаж желаете осмотреть? ", ))
    h2.go_to(new_floor)
elif name == "ЖК-3":
    new_floor = int(input("Какой этаж желаете осмотреть? ", ))
    h3.go_to(new_floor)
else :
    print("Такого жилого комплекса нет")


