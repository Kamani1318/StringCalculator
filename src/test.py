import re
str = '1\n2,3'
numbers = re.split(",|\n",str)
print(numbers)
print(str)