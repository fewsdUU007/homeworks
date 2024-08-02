class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.num_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor>self.num_of_floors or new_floor <= 0:
            print('ТАКОГО ЭТАЖА НЕ СУЩЕСТВУЕТ!')
        else:
            for i in range(1,new_floor+1):
                print(i)
    def __len__(self):
        return self.num_of_floors
    def __str__(self):
        a = "Название: "+self.name+", кол-во этажей: "+str(self.num_of_floors)
        return a

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))