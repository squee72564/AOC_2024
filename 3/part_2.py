import re
import sys

input_file = "test2.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

sum = 0

def do_mul_ops(valid_portion):
    sum = 0

    mul_ops = re.findall(r"mul\(\d+,\d+\)", valid_portion)

    for op in mul_ops:
        num1, num2 = re.search(r"(\d+),(\d+)", op).group().split(",")
        sum += int(num1) * int(num2)

    return sum


def parse_mul_ops_and_add(line, is_activated):
    sum = 0
    
    # when its activated we want to search for a dont() and multiply all operations in between
    # when its not activated we want to search for a do() and ignore operations in between
    # we repeat this until the line is processed

    while line:
        match = None

        if is_activated:
            match = re.search(r"(don't\(\))", line)

            # Here the valid line is everything before the don't(); we are activated
            # so we want to use these mult ops
            if match is not None:
                m_start = match.start(0)
                m_end = match.end(0)

                valid_portion = line[:m_start]
                line = line[m_end:]

                sum += do_mul_ops(valid_portion)
                
                is_activated = False

            else:
                
                # Here we did not find a don't(), so the whole line is valid
                sum += do_mul_ops(line)
                break


        else:
            match = re.search(r"(do\(\))", line)

            # Here we are not activated so we just look for a do(), and when we find
            # one we re-activate and use everything after the do() as the valid line
            if match is not None:

                m_start = match.start(0)
                m_end = match.end(0)

                line = line[m_end:]

                is_activated = True

            else:

                # Here we do not find the do() command anywhere in the line so we are still
                # deactivated with nothing to do; break and continue on next line
                break

    return (sum, is_activated)

with open(input_file) as file:
    lines = file.readlines()
    
    is_activated = True

    for line in lines:
        line_sum, is_activated = parse_mul_ops_and_add(line, is_activated)

        sum += line_sum

print(sum)
