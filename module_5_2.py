# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:


class House :
    def __init__(self, name, number_of_floors, new_floor) :
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = new_floor
        #print("Из def __init__(self, name, number_of_floors, new_floor)",
        # self.name,self.number_of_floors, self.new_floor)
    def __len__(self ):
        #print("Из def __len__(self )")
        #print("Количество этажей здания в комплексе ", self.name, " равно  ", self.number_of_floors )
        return str(self.number_of_floors)
    def __str__(self ) :
        res = self.name + " " + str(self.number_of_floors)
        #print("Из def __str__(self ) :", res)
        return res
h1 = House("ЖК-1", 5, new_floor = 6)
h2 = House("ЖК-2", 7, new_floor = 1)
h3 = House("ЖК-3", 11, new_floor = 1)

print("h1 = ", h1)
print("h2 = ", h2)
print("h3 = ", h3)
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
print("h1.__len__() = ", h1.__len__())
print("h2.__len__() = ", h2.__len__())
print("h3.__len__() = ", h3.__len__())
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
print("h1.__str__() :", h1.__str__())
print("h1.__str__() :", h2.__str__())
print("h1.__str__() :", h3.__str__())
print("new_floor in h1 = ", h1.new_floor)

