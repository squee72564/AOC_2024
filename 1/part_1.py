import sys

file_name = "test.txt"

if len(sys.argv) > 1:
    file_name = sys.argv[1]

list1 = []
list2 = []

with open(file_name) as file:
    data = file.readlines()
    
    for line in data:
        word1,  word2 = line.split()
        list1.append(int(word1))
        list2.append(int(word2))

list1.sort()
list2.sort()

total_distance = 0

for word1, word2 in zip(list1, list2):
    total_distance += abs(word1 - word2)

print(f"The total distance is : {total_distance}.")

