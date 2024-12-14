import sys

input_file = "test.txt"

if  len(sys.argv) > 1:
    input_file = sys.argv[1]

towers = {}
taken_spaces = {}
score = 0
h,w = 0,0

with open(input_file) as file:
    lines = [[c for c in line.strip()] for line in file.readlines()]
    h,w = len(lines), len(lines[0])
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                if char not in towers:
                    towers[char] = [(i,j)]
                else:
                    towers[char].append((i,j))

for tower, positions in towers.items():

    for i, position in enumerate(positions):
        for j, other_position in enumerate(positions):
            if other_position == position:
                continue
            x,y = position
            
            dx = position[0] - other_position[0]
            dy = position[1] - other_position[1]

            while x >= 0 and x < h and y >= 0 and y < w:
                if (x,y) not in taken_spaces:
                    if lines[x][y] ==  '.':
                        lines[x][y] = '#'
                    taken_spaces[x,y] = True
                    score += 1

                x -= dx
                y -= dy

for line in lines:
    print(''.join(line))

print(score)
