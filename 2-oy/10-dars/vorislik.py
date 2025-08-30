"""
vorislik
"""

class Transport:
    def __init__(self, nomi):
        self.nomi = nomi


class Car(Transport):
    def harakat(self):
        return f"{self.nomi} bu transport yolda harakatlanandi"


class Plane(Transport):
    def harakat(self):
        return f"{self.nomi} bu transport yolda harakatlanandi"


car = Car("BMW")
plane = Plane("b2")
print(car.harakat())
print(plane.harakat())