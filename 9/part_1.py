import sys

input_file = "test.txt"

if len(sys.argv) > 1:
    input_file = sys.argv[1]

blocks = []
score = 0

with open(input_file) as file:
    line = file.read().strip()

    if len(line) % 2 != 0:
        line += '0'
    
    for i in range(0, len(line), 2):
        block_sz =  int(line[i])
        free_space = int(line[i+1])

        for j in range(block_sz):
            blocks.append(i//2)

        for j in range(free_space):
            blocks.append(-1)

def find_next_free(blocks, j):
    for i in range(j+1, len(blocks)):
        if blocks[i] == -1:
            return i
    return -1

def find_last_block(blocks, j):
    for i in range(j-1, -1, -1):
        if blocks[i] != -1:
            return i

    return -1

l, r = find_next_free(blocks, -1), find_last_block(blocks, len(blocks))

while l < r:
    blocks[l], blocks[r] = blocks[r], blocks[l]
    l, r = find_next_free(blocks,l), find_last_block(blocks,r)

for i in range(len(blocks)):
    if blocks[i] == -1:
        break

    score += i * blocks[i]


print(score)
