from abc import ABC, abstractmethod
class Father(ABC):
    def __init__(self, name):
        self.name = name

        @abstractmethod
        def loan(self):
            pass


class Venkatesh(Father):
    def loan(self):
        print("loan given")


Venkat = Venkatesh("rancho")
Venkat.loan()
