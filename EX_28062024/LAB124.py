class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model
    def start_engine(self):
        print("starting the car with the name" + self.name)
        print("starting the car with the make" + self.make)
        print("starting the car with the model" + self.model)

Lambo = Car("Lambo", "V2", "2024")
Lambo.start_engine()