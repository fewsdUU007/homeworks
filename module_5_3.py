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

    def __eq__(self,other):
        if isinstance(other, House) == True:
            if self.__len__()==other.__len__():
                return True
            else:
                return False
        else:
            print('Невозможно сравнить эти обекты')
    def __it__(self,other):
        if isinstance(other, House) == True:
            if self.__len__()<other.__len__():
                return True
            else:
                return False
        else:
            print('Невозможно сравнить эти обекты')
    def __le__(self,other):
        if isinstance(other, House) == True:
            if self.__len__()<=other.__len__():
                return True
            else:
                return False
        else:
            print('Невозможно сравнить эти обекты')
    def __gt__(self,other):
        if isinstance(other, House) == True:
            if self.__len__()>other.__len__():
                return True
            else:
                return False
        else:
            print('Невозможно сравнить эти обекты')
    def __ge__(self,other):
        if isinstance(other, House) == True:
            if self.__len__()>=other.__len__():
                return True
            else:
                return False
        else:
            print('Невозможно сравнить эти обекты')
    def __ne__(self,other):
        if isinstance(other, House) == True:
            if self.__len__()!=other.__len__():
                return True
            else:
                return False
        else:
            print('Невозможно сравнить эти обекты')

    def __add__(self,other):
        if isinstance(other, int) == True:
            self.num_of_floors=self.num_of_floors + other
            return self
        else:
            print('Невозможно совместить эти обекты')
    def __radd__(self,other):
        return self.__add__(other)
    def __iadd__(self,other):
        return self.__add__(other)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1.__str__())
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__