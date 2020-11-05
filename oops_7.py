# ABSTRACT BASE CLASS and @abstractmethod

from abc import ABC,abstractmethod

class Order(ABC):

    @abstractmethod
    def print_square(self):
        pass

class Square(Order):

    def __init__(self, side):
        self.side = side

    def print_square(self):
        return "The square is", self.side*self.side

side1 = Square(8)

print(side1.print_square())