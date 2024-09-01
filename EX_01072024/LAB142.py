class GF:
    def car(self):
        return "ambassidor"

class F(GF):
    def car(self):
        return "Swift dezire"

class S(F):
    def car(self):
        return "Lambo"


s = S()
print(s.car())
f = F()
print(f.car())
gf = GF()
print(gf.car())