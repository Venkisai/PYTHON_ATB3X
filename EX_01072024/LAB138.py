class Father:
    def Father_money(self):
        return "5"
    def home(self):
        return "This is from Father"

class Mother:
    def Mother_money(self):
        return "2"
    def home(self):
        return "This is from Mother"

class Son(Mother, Father):
    def home(self):
        return "Took total for playing games"


child = Son()
print(child.home())
print(child.Father_money())
print(child.Mother_money())