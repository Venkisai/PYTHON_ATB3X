from abc import ABC, abstractmethod
class PyATB(ABC):
    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Yejas(PyATB):
    def payFee(self):
        print("paid")


yejas = Yejas()
yejas.enrolled()