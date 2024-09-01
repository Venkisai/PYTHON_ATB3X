class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):
        super().home()
        print("No House")


Venkat = Son()
print(Venkat.home())
