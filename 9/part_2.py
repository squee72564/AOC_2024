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


def find_free_space(blocks, j):
    first_free_idx = -1
    for i in range(j+1, len(blocks)):
        if first_free_idx == -1 and blocks[i] == -1:
            first_free_idx = i
        elif first_free_idx != -1 and blocks[i] != -1:
            return (first_free_idx, i-1)

    return (-1,-1)

def find_next_block(blocks, j):
    last_block_idx = -1
    block_id = -1
    for i in range(j-1, -1, -1):
        if last_block_idx == -1 and blocks[i] != -1:
            last_block_idx = i
            block_id = blocks[i]
        elif last_block_idx != -1 and blocks[i] == -1 or blocks[i] != block_id:
            return (i+1, last_block_idx)

    return (-1,-1)

l, r = -1, len(blocks)

while r >= 0:
    # get the file block (descending ID)
    startb,endb = find_next_block(blocks,r)

    # scan for a free space that matches the block size
    startf,endf = find_free_space(blocks,l)

    # while we do not have a large enough free space we keep looking
    while (endb-startb) > (endf-startf) and startb > endf and (startf,endf) != (-1,-1):
        startf,endf = find_free_space(blocks,endf)

    # when we have a block size that can accomodate it, we move it
    if (endb-startb) <= (endf-startf) and startb > endf:
        blocks[startf:startf+endb-startb+1], blocks[startb:endb+1] = blocks[startb:endb+1], blocks[startf:startf+endb-startb+1]

    # continue to the next file
    r = startb


for i in range(len(blocks)):
    if blocks[i] != -1:
        score += i * blocks[i]

print(score)
