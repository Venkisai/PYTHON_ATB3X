class Math():
    def add(self, a, b = 0, c = 0):
        return a + b + c

    #def add(self,a,c):
       # return self.a + self.c


math = Math()
op0 = math.add(2)
op1 = math.add(2,3)
op2 = math.add(2,3,4)
print(op0)
print(op1)
print(op2)