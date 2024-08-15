class Myclass:

    def __init__(self):
        self.name = "Venkat"

    def public_func(self):
        print("I am public_func()")

    def __private_func(self):
        print("You can put this as private()")

    def public_func_private(self):
        self.__private_func()


a = Myclass()
a.public_func()
a.public_func_private()