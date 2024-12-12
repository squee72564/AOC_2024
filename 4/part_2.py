import sys

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

score = 0

def check(i,j,grid):
    sum = 0

    t, b, l, r = i-1, i+1, j-1, j+1

    if t < 0 or b >= len(grid) or l < 0 or r >= len(grid[0]):
        return 0

    chars = ['M','S']
    check = [grid[t][l], grid[b][l], grid[t][r], grid[b][r]]

    # check if diagonals have correct potential characters
    for diagonal in check:
        if diagonal not in chars:
            return 0

    # All the diagonals have a M or S, so make sure that the
    # diagonals are not equal to each other
    if check[0] == check[3] or check[1] == check[2]:
        return 0

    return 1

with open(input_file) as file:
    lines = file.readlines()
    grid = []

    for line in lines:
        grid.append(line.strip())

    # process the grid character by character
    #   - When we hit an 'A', we want to check and see if we have an X-MAS
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'A':
                score += check(i,j,grid)

print(score)
