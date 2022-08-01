class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power) -> None:
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        fuel_needed = kilometers * self.__class__.DEFAULT_FUEL_CONSUMPTION
        if self.fuel < fuel_needed:
            return

        self.fuel -= fuel_needed