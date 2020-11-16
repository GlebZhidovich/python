class Vehicle:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def beep(self):
        print(f"{self.name} beep!!!")

    def __str__(self):
        return f"Name: {self.name}, Weight: {self.weight}"



class Ship(Vehicle):

    def __init__(self, *args, luggage, **kwargs):
        super().__init__(*args, **kwargs)
        self.luggage = luggage

    def show_luggage(self):
        print(self.luggage)

    def __str__(self):
        return f"Name: {self.name}, Weight: {self.weight}, Luggage: {self.luggage}"


class Car(Vehicle):

    def __init__(self, *args, wheels,**kwargs):
        super().__init__(*args, **kwargs)
        self.wheels = wheels

    def __str__(self):
        return f"Name: {self.name}, Weight: {self.weight}, Wheels: {self.wheels}"


