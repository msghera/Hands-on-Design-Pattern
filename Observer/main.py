from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class IphoneStrore(Subject):

    def __init__(self, in_stock: int = 0) -> None:
        self.observers: List[Observer] = []

        self.in_stock = in_stock

    def re_stock(self, new_stock: int = 0) -> None:
        self.in_stock += new_stock
        print(f'Iphone is restocked with {new_stock} new stock.')
        self.notify()

    def stock_out(self) -> None:
        self.in_stock = 0

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)
    
    def notify(self) -> None:
        if self.in_stock > 0:
            for observer in self.observers:
                observer.update()


class Person(Observer):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return str(self.name)

    def update(self) -> None:
        print (f'{self} gets an update of new stock.')


if __name__ == '__main__':
    iphone = IphoneStrore()

    karim = Person('Karim')
    rahim = Person('Rahim')
    ghazanfar = Person('Ghazanfar')

    iphone.re_stock(10)

    iphone.attach(karim)
    iphone.re_stock(2)

    iphone.attach(ghazanfar)
    iphone.re_stock(3)

    iphone.detach(karim)
    iphone.re_stock(5)


