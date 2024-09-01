my_dict = {
    'b' : 2,
    'a' : 1,
    'c' : 3
}


for k,v in my_dict.items():
    if k == 'b':
        print("key with name b is found")

O = 'b' in my_dict
print(O)