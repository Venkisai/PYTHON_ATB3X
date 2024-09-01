My_details =\
    {"name": "Venkatesh",
     "Height": 5.7,
     "Weight": 104,
     "Married": True,
     "Area": "Hyderabad"
     }
print(My_details.get("name"))
print(My_details.get("Area"))
print(My_details["Area"])
print(My_details.values())
print(My_details.keys())



D = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'a': 10}
print(D)
print(len(D))
print(list(D.values()))
print(list(D.keys()))
for k, v in D.items():
 print(k,v)