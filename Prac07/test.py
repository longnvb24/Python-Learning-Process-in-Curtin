class Vehicle:
    def start(self):
        print("Vehicle starting")
class Car(Vehicle):
    def start(self):
        print("Car starting")
class Truck(Vehicle):
    def start(self):
        print("Truck starting")
class CyberTruck(Car, Truck):
    pass
ct = CyberTruck()
ct.start()