import os

# Get the directory of this script and join it with "input.txt"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    data = f.read()

# Solve part 1 of the problem
part1Result = data.count('(') - data.count(')')
print(f"Floors: {part1Result}")

# Solve part 2 of the problem
part2Result = 0
for i, char in enumerate(data):
    if char == '(':
        part2Result += 1
    else:
        part2Result -= 1

    if part2Result == -1:
        print(f"First basement entry at position: {i + 1}")
        break