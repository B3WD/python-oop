from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer
from project.gym import Gym


# c1 = Customer("Alan", "str123", "lol@lol.xd")
# c2 = Customer("Kay", "mk387465", "cool@email.nice")
# print(c1)
# print(c2)

# e1 = Equipment("Skies")
# e2 = Equipment("Rollers")
# print(e1)
# print(e2)

# ep1 = ExercisePlan(1, 1, 45)
# ep2 = ExercisePlan.from_hours(2, 2, 2)
# print(ep1)
# print(ep2)

# s1 = Subscription("01.01.2022", 1, 1, 1)
# s2 = Subscription("02.02.2022", 2, 2, 2)
# print(s1)
# print(s2)

# t1 = Trainer("Ivan")
# t2 = Trainer("Kosio")
# print(t1)
# print(t2)

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))