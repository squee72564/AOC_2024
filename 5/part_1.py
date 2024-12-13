import sys

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]


before_rules = {}
after_rules = {}
tests = []
sum = 0

with open(input_file) as file:

    lines = file.readlines()

    rules = True

    for line in lines:
        if line == '\n':
            rules = False
            continue

        line = line.strip()

        if rules:
            # First lets get the rules
            rules = line.split("|")
            before, after = int(rules[0]), int(rules[1])
            
            if before in before_rules:
                before_rules[before].append(after)
            else:
                before_rules[before] = [after]

            if after in after_rules:
                after_rules[after].append(before)
            else:
                after_rules[after] = [before]

        else:
            # Then lets get the test cases
            tests.append([int(x) for x in line.split(',')])

for test in tests:
    is_bad = False
    for i, curr in enumerate(test):
        for j, check in enumerate(test):
            if i == j:
                continue

            if i > j: # before the curr
                if check in before_rules and curr not in before_rules[check]:
                    is_bad = True
                    break
            else: #after the curr
                if check in after_rules and curr not in after_rules[check]:
                    is_bad = True
                    break
        if is_bad:
            break
    
    if not is_bad:
        sum += test[len(test)//2]
        
print(sum)
