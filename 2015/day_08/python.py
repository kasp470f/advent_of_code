import os

# Get the directory of this script and join it with "input.txt"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    data = f.read()
    
# Solve part 1 of the problem
lines = data.splitlines()
memory_characters = sum([len(line) for line in lines])

string_literals = sum([len(eval(line)) for line in lines])
print(f"Part 1: {memory_characters - string_literals}")

# Solve part 2 of the problem
part_2_memory_characters = sum([len(line) + 2 + line.count('\\') + line.count('"') for line in lines])
string_literals = sum([len(line) for line in lines])
print(f"Part 2: {part_2_memory_characters - string_literals}")
