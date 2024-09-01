class A:
    def method(self):
        return "methodA"

class B:
    def method(self):
        return "methodB"

class C(A,B):
    pass

class C(B,A):
    pass


object = C()
print(object.method())
print(object.method())
