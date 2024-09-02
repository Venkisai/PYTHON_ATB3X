class Person:
    name = None
    Id = None
    address = None
    city = None


    def talk(self):
        print("I can talk")

    def sleep(self, name):
        print("I am a method")
        print("I am sleeping", name)


    def walk(self):
        print("I am walking")
        return None

    def run_return(self, name):
        print("I can run also")
        return "I am running"


Venkat = Person()
Venkat.name = "Venkat duguru"
Venkat.talk()


Ramya = Person()
Ramya.name = "Doguru Ramya"
Ramya.walk()