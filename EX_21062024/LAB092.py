t = ("The testing academy", "for", "Automation Testing", "The testing academy")
S = set(t)
print(S)
print(len(S))
#Here t contains 4 items
#but S contains 3 items only why because set does not allows duplicate items
S1 = {1, 2, 3}
S2 = {4, 5, 6}
S3 = S1.union(S2)
print(S3)

S4 = {1, 2, 3, 4, 5}
S5 = {4, 5, 6, 7, 8}
S6 = S4.intersection(S5)
print(S6)
S7 = S4.union(S5)
print(S7)

S8 = S4.difference(S5)
S9 = S5.difference(S4)
print(S8)
print(S9)
