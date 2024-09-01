from abc import ABC, abstractmethod
class ATB(ABC):
    @abstractmethod
    def perform_task1(self):
        pass
    def perform_task2(self):
        pass

class Amit(ATB):
    def perform_task1(self):
        return "Done 1"

    def perform_task2(self):
        return "Done 2"


amit = Amit()
print(amit.perform_task1())
print(amit.perform_task2())