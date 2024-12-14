import sys

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

grid = []
visited = set()

def get_starting_position(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return (i,j)

    return (-1,-1)

with open(input_file) as file:
    lines = file.readlines()

    for line in lines:
        grid.append(line.strip())


x, y = get_starting_position(grid)

delta = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1],
]
curr_dir = 0

score = 0

def check_oob(x,y,grid):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

while check_oob(x,y,grid):

    if (x,y) not in visited:
        score += 1
        visited.add((x,y))

    dx, dy = x + delta[curr_dir][0], y + delta[curr_dir][1] 

    if check_oob(dx,dy,grid) and grid[dx][dy] == '#':
        curr_dir = (curr_dir + 1) % 4
    else:
        x, y = dx, dy

print(score)
    

