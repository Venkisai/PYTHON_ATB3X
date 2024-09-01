class Gopal:
    def BHK1(self):
        print("1BHK")

class Dhruva(Gopal):
    def BHK2(self):
        print("2BHK")

class Venkatesh(Gopal):
    def BHK3(self):
        print("3BHK")

class Srikanth(Gopal):
    def No_House(self):
        print("No_House")


Family = Gopal()
Family.BHK1()

Family = Dhruva()
Family.BHK2()
Family.BHK1()

Family = Venkatesh()
Family.BHK3()
Family.BHK1()

Family = Srikanth()
Family.No_House()
Family.BHK1()