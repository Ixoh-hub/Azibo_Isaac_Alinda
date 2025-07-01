class Vehicle:
    def info(self):
        print("Requires Energy")
        
class Car:
    def info(self):
        print("Requires Petrol gen Energy")
        
class Tesla:
    def info(self):
        print("Requires Electric Energy")

class ModernCar(Car, Tesla):
    pass

CyberTruck = ModernCar()
CyberTruck.info()
print(ModernCar.__mro__)