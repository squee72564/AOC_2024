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

def reorder(test):
    reordered = []
    
    while len(test) > 0:
        for i, t in enumerate(test):
            if all(x not in before_rules or t not in before_rules[x] for x in test):
                reordered.append(t)
                test.pop(i)
                break

    return reordered

for test in tests:
    is_reordered = False
    for i, curr in enumerate(test):
        for j, check in enumerate(test):
            if i == j:
                continue

            if i > j: # before the curr
                if check in before_rules and curr not in before_rules[check]:
                    test = reorder(test)
                    is_reordered = True
                    break
            else: #after the curr
                if check in after_rules and curr not in after_rules[check]:
                    test = reorder(test)
                    is_reordered = True
                    break

        if is_reordered:
            break

    if is_reordered:
        sum += test[len(test)//2]
        
print(sum)
