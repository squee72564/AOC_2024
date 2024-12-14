import sys
from itertools import product 

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

def combine_operators(line):
    res, nums = line.split(":")
    res = int(res.strip())
    nums = [int(n) for n in nums.strip().split()]

    prod = list(product(["+","*"], repeat=len(nums)-1))

    for operators in prod:

        intermediate_num = nums[0]
        for i, op in enumerate(operators):
            if op == '+':
                intermediate_num += nums[i+1]
            else:
                intermediate_num *= nums[i+1]

        if intermediate_num == res:
            return res

    return 0

score = 0

with open(input_file) as file:
    lines = file.readlines()

    for line in lines:
        score += combine_operators(line)            

print(score)
