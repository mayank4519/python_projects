class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def addCar(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add {car.__class__.__name__} to the garage, but can add only Car objects')

        self.cars.append(car)


ford = Car('Ford', 'Fiesta')
mygarage = Garage()
try:
    mygarage.addCar(ford)
except TypeError:
    print("Your car is not a Car!")
except ValueError:
    print("Its a value error...")
finally:
    print(f"garage length is {len(mygarage)}")
