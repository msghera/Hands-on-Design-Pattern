from abc import ABC, abstractmethod

# class Mammals(ABC):
#     @abstractmethod
#     def swim() -> bool:
#         print("Can Swim") 

#     @abstractmethod
#     def walk() -> bool:
#         print("Can Walk") 

# class Human(Mammals):
#     def swim():
#         return print("Humans can swim") 

#     def walk():
#         return print("Humans can walk") 

# class Whale(Mammals):
#     def swim():
#         return print("Whales can swim") 


# Human.swim()
# Human.walk()

# Whale.swim()
# Whale.walk()


class Walker(ABC):
    @abstractmethod
    def walk() -> bool:
        print("Can Walk") 

class Swimmer(ABC):
    @abstractmethod
    def swim() -> bool:
        print("Can Swim") 

class Human(Walker, Swimmer):
    def walk():
        print("Humans can walk") 
    def swim():
        print("Humans can swim") 

class Whale(Swimmer):
    def swim():
        print("Whales can swim") 


Human.walk()
Human.swim()

Whale.swim()
Whale.walk()

