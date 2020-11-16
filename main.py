from vehicle import *

try:
    car = Car("Honda", 2000, wheels=3)
    vehicle = Vehicle('Bicycle', 20)
    ship = Ship('Titanic', 15000, luggage=['tooth', 'jacket'])
    print(vehicle)
    print(ship)
    print(car)
    ship.show_luggage()
except Exception:
    print('hi')