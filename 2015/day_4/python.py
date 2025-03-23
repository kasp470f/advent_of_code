import os
import hashlib

# Get the directory of this script and join it with "input.txt"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    data = f.read()
    
# Solve part 1 of the problem

def findZeros(data, zeros):
    count = 0
    while True:
        string_to_hash = data + str(count)
        hash_result = hashlib.md5(string_to_hash.encode()).hexdigest()
        if hash_result.startswith(zeros):
            break
        
        count += 1
    return count

print("Part 1:", findZeros(data, '00000'))
print("Part 2:", findZeros(data, '000000'))
