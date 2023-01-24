import re
from functools import reduce


def sum(x, y):
    return int(x) + int(y)


def extract_delimiter(line):
    if line[2] == '[':
        new_delimiter = str(re.findall(r"\[([^\]]+)\]", line))
        return new_delimiter
    else:
        return line[2]

def generate_error_for_negative_numbers(sums_per_line):
    for i in sums_per_line:
        if i < 0:
            raise ValueError('negatives not allowed')


def string_calc(str):
    if str == "":
        return 0
    else:
        delimiter = ","
        lines = re.split("\n", str)
        sums_per_line = []
        for line in lines:
            if line.startswith("//"):
                delimiter = extract_delimiter(line)
                continue
            if line.endswith(delimiter):
                raise ValueError('line cant end with delimiter')
            list_of_numbers = re.findall(r'-?\d+\.?\d*', line)
            numbers = [int(i) for i in list_of_numbers]
            sums_per_line.extend(numbers)
            generate_error_for_negative_numbers(sums_per_line)
            sums_per_line = [i for i in sums_per_line if i<1000]
        return reduce(lambda acc, iter: acc + iter, sums_per_line)
