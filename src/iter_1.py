import re
from functools import reduce
def sum(x,y):
    return int(x) + int(y)
def string_calc(str):
    if str == "":
        return 0
    else:
        delimiter = ","
        lines = re.split("\n",str)
        sum = []
        for line in lines:
            if line.startswith("//"):
                delimiter = line[2]
                continue
            numbers = re.split(delimiter,line)
            num = [int(i) for i in numbers]
            sum.extend(num)
            for i in sum:
                if i<0:
                    raise ValueError('negatives not allowed')
        return reduce(lambda acc,iter: acc + iter,sum)
            
    


            
                
    