class Calc:

    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b


object_ref = Calc()
A = object_ref.sum(3,4)
print(A)