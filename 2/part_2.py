import sys

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

def check_safe(levels):
    deltas = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    if  (all(x < 0 and x in range(-3,0) for x in deltas) or
         all(x > 0 and x in range(1,4) for x in deltas)):
        return True
    else:
        return False

        
safe_lines = 0

with open(input_file) as file:
    lines = file.readlines()
    
    for line in lines:
        levels = [int(level) for level in line.strip().split()]

        if check_safe(levels):
            safe_lines += 1
        else:
            for i in range(len(levels)):
                temp_level = levels.copy()
                temp_level.pop(i)
                if check_safe(temp_level):
                    safe_lines += 1
                    break
    
print(f"\nsafe lines: {safe_lines}")


