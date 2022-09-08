'''
Полиморфизм это получение различных результатов от одного и того же метода,
в зависимости от объекта, в котором он был вызван.
'''


#  1st sample
class Vehicle:
    def __init__(self, weight, height) -> None:
        self.weight = weight
        self.height = height


class Car(Vehicle):
    def drive(self):
        return self.weight * self.height

    def __str__(self) -> str:
        return 'Машина едет очень быстро.'


class Truck(Vehicle):
    def drive(self):
        return self.weight * self.height

    def __str__(self) -> str:
        return 'Грузовик едет очень медленно.'


# c = Car(25, 30)
# t = Truck(80, 90)
# print(c.drive())
# print(t.drive())
