import re
from functools import reduce
def sum(x,y):
    return int(x) + int(y)
def string_calc(str):
    if str == "":
        return 0
    else:
        numbers = re.split(",|\n",str)
        res = [eval(i) for i in numbers]
        print(res)
        return reduce(lambda x,y: x + y, res)


            
                
    