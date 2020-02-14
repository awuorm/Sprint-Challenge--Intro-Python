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


class Vehicle():
    def __init__(self, vehicle):
        self.vehicle = vehicle
    def makevehicle(self):
        self.vehicle
    pass


class GroundVehicle(Vehicle):
    def __init__(self, groundvehicle):
        self.groundvehicle = groundvehicle
    pass

class Car(GroundVehicle):
    def __init__(self,car):
        self.car = car
    pass
class Motorcycle(GroundVehicle):
    def __init__(self,motorcycle):
        self.motorcycle = motorcycle
    pass


class FlightVehicle():
    def __init__(self,flightvehicle):
        self.flightvehicle = flightvehicle
    #     self.wings = wings
    # def makeairplane(self,Vehicleengine,Vehiclewheels):
    #     plane = self.autopilot + Vehicleengine + Vehiclewheels
    #     return plane
    pass
class Airplane(FlightVehicle):
    def __init__(self,airplane):
        self.airplane = airplane
    pass

class Starship():
    def __init__(self,starship):
        self.starship = starship
    def makestarship(self,Vehiclevehicle):
        self.starship = Vehiclevehicle
        print(self.starship)
    # pass

# class A(object):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def addNums():
#         self.b + self.c

# class B(object):
#     def __init__(self, d, e):
#         self.d = d
#         self.e = e

#     def addAllNums(self, Ab, Ac):
#         x = self.d + self.e + Ab + Ac
#         return x
