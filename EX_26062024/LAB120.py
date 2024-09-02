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




print(Calc(7,8).sum())
print(Calc(7,8).sub())
print(Calc(7,8).mul())
print(Calc(7,8).div())