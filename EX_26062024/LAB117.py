class Dog:
    name = None
    Id = None

    def __init__(self,name,Id):
        self.name = name
        self.Id = Id

    def sleep(self):
        print("sleeping")


dog1 = Dog('Wow', 508)
print(dog1.name)
print(dog1.Id)
