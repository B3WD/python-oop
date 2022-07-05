from project.customer import Customer
from project.dvd import DVD
# from customer import Customer
# from dvd import DVD

class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers = [] # holds Customer objects
        self.dvds = [] # holds DVD objects

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def find_customer_by_id(self, customer_id) -> Customer:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def find_dvd_by_id(self, dvd_id: int) -> DVD:
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_obj = self.find_customer_by_id(customer_id)
        dvd_obj = self.find_dvd_by_id(dvd_id)

        if dvd_obj in customer_obj.rented_dvds:
            return f"{customer_obj.name} has already rented {dvd_obj.name}"

        if dvd_obj.is_rented:
            return "DVD is already rented"

        if customer_obj.age < dvd_obj.age_restriction:
            return f"{customer_obj.name} should be at least {dvd_obj.age_restriction} to rent this movie"

        dvd_obj.is_rented = True
        customer_obj.rented_dvds.append(dvd_obj)
        return f"{customer_obj.name} has successfully rented {dvd_obj.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer_obj = self.find_customer_by_id(customer_id)
        dvd_obj = self.find_dvd_by_id(dvd_id)

        if dvd_obj not in customer_obj.rented_dvds:
            return f"{customer_obj.name} does not have that DVD"

        customer_obj.rented_dvds.remove(dvd_obj)
        dvd_obj.is_rented = False
        return f"{customer_obj.name} has successfully returned {dvd_obj.name}"

    def __repr__(self) -> str:
        msg = "\n".join([repr(c) for c in self.customers])
        msg += "\n" + "\n".join([repr(d) for d in self.dvds])
        return msg

        
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)

# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

# movie_world = MovieWorld("The Best Movie Shop")

# movie_world.add_customer(c1)
# movie_world.add_customer(c2)

# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)

# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))

# print(movie_world)