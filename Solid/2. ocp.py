from vars import *
from abc import abstractmethod, ABC

class CalcOperation(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def operation(first_var: float, second_var: float):
        pass

class Add(CalcOperation):
    def operation(first_var: float, second_var: float)->None:
        return first_var + second_var

class Substract(CalcOperation):
    def operation(first_var: float, second_var: float)->None:
        return first_var - second_var


print(f'Add : {Add.operation(var1, var2)}')
print(f'Substract : {Substract.operation(var1, var2)}')

class Multiply(CalcOperation):
    def operation(first_var: float, second_var: float)->None:
        return first_var * second_var


# class Divide(CalcOperation):
#     def operation(first_var: float, second_var: float)->None:
#         return first_var / second_var

for operation in CalcOperation.__subclasses__():
    res = operation.operation(var1, var2)
    print(f'{operation.__name__} : {res}')
