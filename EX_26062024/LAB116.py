class Dog:
    name = None
    Id = None

    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

    def sleep(self):
        print("who is sleeping --->" + self.name)


dog1 = Dog('Chow', 248)
dog2 = Dog('Mow', 551)

print(f'{dog1.name} has Id {dog1.Id}')
print(f'{dog2.name} has Id {dog2.Id}')

dog1.sleep()
dog2.sleep()