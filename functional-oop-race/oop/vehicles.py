"""
Vehicles including cars, motorbikes , ...
"""


class Vehicle:
    def __init__(self, name, speed=1.0):
        self.name = name
        self.speed = speed
        self.location = 0

    def tick(self):
        # x = a.t^2 + v0.t + x0
        # x = v0.t
        self.location = self.location + self.speed


class Car(Vehicle):
    def __init__(self, name, speed=1.0):
        super().__init__(name, speed)
        # very safe :
        self.seatbelts = True
        self.trunk = "closed"

    def open_trunk(self):
        self.trunk = "open"
        print("bunch of stuff")
        print("also spare tire")


class Cheater(Car):
    def __init__(self, name, speed=1.0):
        super().__init__(name, speed)
        self.location = 1000000


class Motorbike(Vehicle):
    def __init__(self, name, speed=1.0, t_angle=60):
        super().__init__(name, speed)
        # also, very safe
        self.helmet = True
        self.angle = 0.0
        self.t_angle = t_angle

    def takcharkh(self):
        if self.speed > 12 and self.helmet == True:
            self.angle = self.t_angle

