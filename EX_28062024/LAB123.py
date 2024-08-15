class Person:

    name = "Venky"
    age = None

    def walk(self):
        a = 10
        print("Hi I am a method")
        print("Hi", self.age)


object = Person()
object.walk()