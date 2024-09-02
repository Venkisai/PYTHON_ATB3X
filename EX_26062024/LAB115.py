class Dog:
    name = None
    Id = None


    def sleep(self):
        print("Its a sleepy dog")


dog1 = Dog()
print(dog1.name)
dog1.name = "chow"
dog1.Id = 248
print(dog1.name)
print(dog1.Id)
dog1.sleep()