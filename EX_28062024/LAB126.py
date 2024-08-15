#Encapsulation
#bind the data variables in with the methods
class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when an object is created")

    def change_password(self):
        self.password = "345"


XUV = Car()
XUV.change_password = "345"