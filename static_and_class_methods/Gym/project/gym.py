# from customer import Customer
# from trainer import Trainer
# from equipment import Equipment
# from exercise_plan import ExercisePlan
# from subscription import Subscription

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self) -> None:
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_item(item_id: int, source: list):
        for item in source:
            if item.id == item_id:
                return item

    @staticmethod
    def add_item(item, source: list):
        if item not in source:
            source.append(item)

    def add_customer(self, customer: Customer):
        self.add_item(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add_item(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add_item(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add_item(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add_item(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        msg = ""
        s = self.get_item(subscription_id, self.subscriptions)
        c = self.get_item(s.customer_id, self.customers)
        t = self.get_item(s.trainer_id, self.trainers)
        p = self.get_item(s.exercise_id, self.plans)
        eq = self.get_item(p.equipment_id, self.equipment)
        msg += repr(s) + '\n' + repr(c) + '\n' + repr(t) + '\n' + repr(eq) + '\n' + repr(p)
        return msg