#result = 10/0
#print(result)#ZeroDivisionError: division by zero
#import non_existent_module#ModuleNotFoundError: No module named 'non_existent_module'
import math
#print(math.exp(1000))OverflowError: math range error
try:
    math.exp(1000)
except Exception as e:
    print(e)
