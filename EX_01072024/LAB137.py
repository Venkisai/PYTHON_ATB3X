class Srinivasan:
    affidivate = "3kg gold"
    def grand_method(self):
        return "Srinivasan's method"

class Gopalan(Srinivasan):
    def father_method(self):
        return "Gopalan's method"

class Venkateshan(Gopalan):
    def child_method(self):
        return "Venkateshan's method"


object = Srinivasan()
print(object.grand_method())

object1 = Gopalan()
print(object1.father_method())
print(object1.grand_method())

object2 = Venkateshan()
print(object2.child_method())
print(object2.grand_method())