# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    # def __init__(self, vehicle):
    #     self.vehicle = vehicle
    pass


class GroundVehicle(Vehicle):
    # def __init__(self, groundvehicle):
    #     self.groundvehicle = groundvehicle
    pass

class Car(GroundVehicle):
    # def __init__(self,car):
    #     self.car = car
    pass
class Motorcycle(GroundVehicle):
    # def __init__(self,motorcycle):
    #     self.motorcycle = motorcycle
    pass


class FlightVehicle(Vehicle):
    # def __init__(self, vehicle):
    #     self.vehicle = vehicle
    pass

class Airplane(FlightVehicle):
    # def __init__(self, vehicle):
    #     self.vehicle = vehicle
    pass

class Starship(FlightVehicle):
    # def __init__(self, vehicle):
    #     self.vehicle = vehicle
    pass
