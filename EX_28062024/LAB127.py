class Car:
    name = None

    def __init__(self):
      self.public_var = "public"
      self._protected_var = "protected123"
      self.__private_var = "pass@123"

    def printName(self):
        if self.__private_var == "pass@123":
            print("Hi, 123")
        else:
            print("I am allowed to public")


Alto = Car()
Alto.printName()
