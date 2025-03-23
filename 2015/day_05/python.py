import os

# Get the directory of this script and join it with "input.txt"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    data = f.read()
    
# Solve part 1 of the problem
def nice_string(str):
    vowels = 'aeiou'
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    count_vowels = sum(1 for c in str if c in vowels)
    has_double = any(str[i] == str[i + 1] for i in range(len(str) - 1))
    has_bad_string = any(bad in str for bad in bad_strings)    
    return count_vowels >= 3 and has_double and not has_bad_string

part1Result = 0
for line in data.splitlines():
    if nice_string(line):
        part1Result += 1
print("Part 1: " + str(part1Result))

# Solve part 2 of the problem
def nice_string2(str):
    has_pair = any(str.count(str[i:i + 2]) > 1 for i in range(len(str) - 1))
    has_repeat = any(str[i] == str[i + 2] for i in range(len(str) - 2))
    return has_pair and has_repeat

part2Result = 0
for line in data.splitlines():
    if nice_string2(line):
        part2Result += 1
print("Part 2: " + str(part2Result))
