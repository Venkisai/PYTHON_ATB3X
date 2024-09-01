class Parent:
    gold = "2kg in gold"
    def BHK2(self):
        print("2BHK")

class child(Parent):
    def BHK3(self):
        print("3BHK")


object = child()
object.BHK3()
object.BHK2()
print(object.gold)

object1 = Parent()
object1.BHK2()
print(object1.gold)