try:
    #while True print("Hello")SyntaxError: invalid syntax
    a = 10/0
    print(a)
except Exception as e:
    print(e)