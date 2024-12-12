import sys

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

score = 0

def check(i,j,grid):
    word = "XMAS"

    sum = 0

    dirs = [
        [1,0],
        [1,1],
        [0,1],
        [-1,1],
        [-1,0],
        [-1,-1],
        [0,-1],
        [1,-1]
    ]


    for dx, dy in dirs:
        x,y = i,j

        for char in word:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != char:
                break

            if grid[x][y] == 'S':
                sum += 1

            x += dx
            y += dy

    return sum

with open(input_file) as file:
    lines = file.readlines()
    grid = []

    for line in lines:
        grid.append(line.strip())

    # process the grid character by character
    #   - When we hit an 'X', we want to start the search in all directions
    #       * continue the search in the same direction until we meet an invalid character
    #           or until we sucessfully terminate
    #       * If we can find 'XMAS' in that direction we add to score, else continue to next direction

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'X':
                score += check(i,j,grid)

print(score)
