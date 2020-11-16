from vehicle import *

vehicle = Vehicle('Bicycle', 20)
ship = Ship('Titanic', 15000, luggage=['tooth', 'jacket'])
car = Car("Honda", 2000, wheels=4)
print(vehicle)
print(ship)
print(car)
ship.show_luggage()