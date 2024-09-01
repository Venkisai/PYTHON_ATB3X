class Grandparent:
    key = "abc@123"
    def grandparent_method(self):
        return "Grandparent's method"

class Father(Grandparent):
    def father_method(self):
        return "parent's method"


Parent = Father()
print(Parent.father_method())
print(Parent.grandparent_method())
print(Parent.key)