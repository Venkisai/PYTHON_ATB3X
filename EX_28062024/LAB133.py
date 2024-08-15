class Dog:
    name = None
    id = None
    def __init__(self, name = 'default', id = '99'):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is sleeping -->" + self.name)

dog1 = Dog("Chow Chow", "a")
dog1.sleep()
dog2 = Dog("Mow Mow", "b")
dog2.sleep()
dog3 = Dog()
dog3.name = "WOW"
dog3.id = "c"

print(f'{dog1.name} has id{dog1.id}')
print(f'{dog2.name} has id{dog2.id}')
print(f'{dog3.name} has id{dog3.id}')