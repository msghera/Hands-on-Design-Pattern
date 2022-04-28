from vars import *
from abc import abstractmethod, ABC

class Employee:

    BONUS_FACTOR = 5e-1

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

class FullTimeEmployee(Employee):
    def __init__(self, name, salary) -> None:
        super().__init__(name, salary)


    def get_bonus(self):
        return self.salary * self.BONUS_FACTOR



mike = FullTimeEmployee('Mike', 10000)
ghazanfar = Employee('Ghazanfar', 8000)

employees = [mike, ghazanfar]

for employee in employees:
    print(f'Bonus of {employee.name} is : {employee.get_bonus()}')



# class Employee:

#     BONUS_FACTOR = 5e-1

#     def __init__(self, name, salary) -> None:
#         self.name = name
#         self.salary = salary

#     @abstractmethod
#     def get_bonus(self):
#         return 0.0

# class FullTimeEmployee(Employee):
#     def __init__(self, name, salary) -> None:
#         super().__init__(name, salary)


#     def get_bonus(self):
#         return self.salary * self.BONUS_FACTOR



# mike = FullTimeEmployee('Mike', 10000)
# ghazanfar = Employee('Ghazanfar', 8000)

# employees = [mike, ghazanfar]

# for employee in employees:
#     print(f'Bonus of {employee.name} is : {employee.get_bonus()}')

