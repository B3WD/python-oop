from project.worker import Worker
from project.animal import Animal

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.animals = []
        self.workers = []
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget

    def __find_worker_by_name(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                return w

    def __sum_attr_of_objects_in_list(self, source: list, attr):
        total = 0

        for x in source:
            total += getattr(x, attr)

        return total

    def __get_total_worker_salaries(self):
        return self.__sum_attr_of_objects_in_list(self.workers, "salary")

    def __get_total_animal_expenses(self):
        return self.__sum_attr_of_objects_in_list(self.animals, "money_for_care")

    def __get_list_of_certain_type_of_obj(self, source, obj_type):
        obj_list = []

        for x in source:
            if type(x).__name__ == obj_type:
                obj_list.append(x)

        return obj_list

    def add_animal(self, animal: Animal, price: int):
        if self.__budget - price < 0:
            return f"Not enough budget"

        if len(self.animals) + 1 > self.__animal_capacity:
            return f"Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) + 1 > self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        w = self.__find_worker_by_name(worker_name)

        if w is None:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(w)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_salary = self.__get_total_worker_salaries()

        if total_salary > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_animal_expenses = self.__get_total_animal_expenses()

        if total_animal_expenses > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_animal_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = self.__get_list_of_certain_type_of_obj(self.animals, "Lion")
        tigers = self.__get_list_of_certain_type_of_obj(self.animals, "Tiger")
        cheetahs = self.__get_list_of_certain_type_of_obj(self.animals, "Cheetah")

        animal_type_names = ["Lion", "Tiger", "Cheetah"]
        animals_lsts = [lions, tigers, cheetahs]

        msg = f"You have {len(self.animals)} animals\n"

        for animal_type, animal_lst in zip(animal_type_names, animals_lsts):
            msg += f"----- {len(animal_lst)} {animal_type}s:\n"
            msg += "\n".join([repr(a) for a in animal_lst]) + "\n"

        return msg.strip()

    def workers_status(self):
        keepers = self.__get_list_of_certain_type_of_obj(self.workers, "Keeper")
        caretakers = self.__get_list_of_certain_type_of_obj(self.workers, "Caretaker")
        vetes = self.__get_list_of_certain_type_of_obj(self.workers, "Vet")

        worker_type_names = ["Keeper", "Caretaker", "Vet"]
        worker_lsts = [keepers, caretakers, vetes]

        msg = f"You have {len(self.workers)} workers\n"

        for worker_type, worker_lst in zip(worker_type_names, worker_lsts):
            msg += f"----- {len(worker_lst)} {worker_type}s:\n"
            msg += "\n".join([repr(w) for w in worker_lst]) + "\n"

        return msg.strip()