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
        row = []
        line = line.strip()
        for char in line:
            row.append(char)
        grid.append(row)


start_x, start_y = get_starting_position(grid)

delta = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1],
]
score = 0

def check_oob(x,y,grid):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            x,y = start_x, start_y
            curr_dir = 0
            grid[i][j] = '#'
            
            while check_oob(x,y,grid):

                # if we are in same spot as before in same direction
                if (x,y,curr_dir) in visited:
                    score += 1
                    break

                # add the current position to map
                visited.add((x,y,curr_dir))

                # next move
                dx, dy = x + delta[curr_dir][0], y + delta[curr_dir][1] 

                # if the next move is in bounds and blocked we rotate
                # otherwise we move forward
                if check_oob(dx,dy,grid) and grid[dx][dy] == '#':
                    curr_dir = (curr_dir + 1) % 4
                else:
                    x,y = dx,dy


            visited.clear()

            grid[i][j] = '.'
    

print(score)
