from project.vehicle import Vehicle
from project.family_car import FamilyCar
from project.sport_car import SportCar

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(149, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

sport_car = SportCar(80, 999)
sport_car.drive(10)
print(sport_car.fuel)
sport_car.drive(10)
print(sport_car.fuel)
print(sport_car.fuel_consumption)