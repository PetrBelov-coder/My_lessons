# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
class House :
    def __init__(self, name, number_of_floors, new_floor) :
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self, number_of_floors):
        self.number_of_floors = number_of_floors
        print("Количество этажей здания ", self.number_of_floors )
    def __str__(self, name, number_of_floors) :
        self.name = name
        self.number_of_floors = number_of_floors
        print("Название комплекса :", self.name, "Этажность : ", self.number_of_floors )

h1 = House("ЖК-1", 5, new_floor = 1)
h2 = House("ЖК-2", 7, new_floor = 1)
h3 = House("ЖК-3", 11, new_floor = 1)

print(h1, "\n" , h2,  "\n" , h3 )
#print(h2)
#print(h3)
#print(len(h1))
#print(len(h2))
#print(len(h3))
#print(str(h1))
#print(str(h2))
#print(str(h3))
