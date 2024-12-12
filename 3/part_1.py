import re
import sys

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

sum = 0

def parse_mul_ops_and_add(line):
    sum = 0

    mul_ops = re.findall(r"mul\(\d+,\d+\)", line)

    for op in mul_ops:
        num1, num2 = re.search(r"(\d+),(\d+)", op).group().split(",")
        sum += int(num1) * int(num2)

    return sum

with open(input_file) as file:
    lines = file.readlines()

    for line in lines:
        sum += parse_mul_ops_and_add(line)

print(sum)
