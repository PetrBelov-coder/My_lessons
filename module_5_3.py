#Задача "Нужно больше этажей":
#Необходимо дополнить класс House следующими специальными методами:
#__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
#Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе
# и возвращать результаты сравнения по соответствующим операторам.
# Как и в методе __eq__ в сравнении участвует кол-во этажей.
#__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
#__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

class House :
    def __init__(self, name, number_of_floors, other, value ) :
        self.name = name
        self.number_of_floors = int(number_of_floors)
        self.other = int(other)
        self.value = int(value)
    def __len__(self, name, number_of_floors ):
        self.number_of_floors = number_of_floors
        print("Количество этажей здания ", self.number_of_floors )
        return self.number_of_floors
    def __str__(self ) :
        #self.name = name
        #self.number_of_floors = number_of_floors
        #print("Название комплекса :", self.name, "Этажность : ", self.number_of_floors )
        res = str(self.name) + " "+ str(self.number_of_floors)
        return res
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
    def __eq__(self, other) :
        if self.number_of_floors == int(other) :
            flag = True
        else :
            flag = False
        #print(flag)
        return flag
#Метод __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
    def __add__(self, value) :
        self.number_of_floors = self.value + self.number_of_floors
        return self.number_of_floors
#Метод __lt__(<) должен присутствовать в классе
    def __lt__(self,number_of_floors, other) :
        if self.number_of_floors < self.other :
            flag = True
            return flag
        else :
            flag = False
            return flag
# Метод __le__(<=) должен присутствовать в классе
    def __le__(self, number_of_floors, other):
        if self.number_of_floors <= self.other:
            flag = True
            return flag
        else:
            flag = False
            return flag
# Метод __ge__(>=) должен присутствовать в классе
    def __ge__(self, number_of_floors, other):
        if self.number_of_floors >= self.other:
            flag = True
            return flag
        else:
            flag = False
            return flag
# Метод __ne__(!=) должен присутствовать в классе
    def __ne__(self, number_of_floors, other):
        if self.number_of_floors != self.other:
            flag = True
            return flag
        else:
            flag = False
            return flag

h1= House("ЖК-1", 5, 5, 10 )
h2= House("ЖК-2", 7, 8, 10)
h3= House("ЖК-3", 11, 10, 10)
print("h1 : ", h1)
print("h2 : ", h2)
print("h3 : ", h3)
print("Этажность : ", h1.__eq__(11))
print("Этажность : ", h2.__eq__(11))
print("Этажность : ", h3.__eq__(11))
h1= House("ЖК-1", 5, 5, 6 )
h2= House("ЖК-2", 7, 8, 4)
h3= House("ЖК-3", 11, 10, 0)
print("Новая этажность : ", h1.__add__(6))
print("Новая этажность : ", h2.__add__(4))
print("Новая этажность : ", h3.__add__(0))


