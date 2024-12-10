import sys

file_name = "test.txt"

if len(sys.argv) > 1:
    file_name = sys.argv[1]

list1 = []
freq_map = {}

with open(file_name) as file:
    data = file.readlines()
    
    for line in data:
        word1, word2 = line.split()
        list1.append(int(word1))
        
        word2 = int(word2)
        
        freq_map[word2] = freq_map.get(word2, 0) + 1

similarity_score = 0

for word in list1:
    if word in freq_map:
        similarity_score += word * freq_map[word]

print(f"The total score is : {similarity_score}.")


