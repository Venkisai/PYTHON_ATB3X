class Calc:
    a = None
    b = None

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b




object = Calc(7,8)
print(object.sum())
print(object.sub())
print(object.mul())
print(object.div())
