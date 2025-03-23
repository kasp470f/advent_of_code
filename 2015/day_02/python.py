import os

# Get the directory of this script and join it with "input.txt"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    data = f.read()

# Solve part 1 of the problem
part1Result = 0;
for line in data.splitlines():
    dimensions = [int(x) for x in line.split('x')]
    dimensions.sort()
    length, width, height = dimensions
    surface_area = 2 * (length * width + width * height + height * length)
    slack = length * width
    part1Result += surface_area + slack
    
print("Part 1: " + str(part1Result))

# Solve part 2 of the problem
part2Result = 0
for line in data.splitlines():
    dimensions = [int(x) for x in line.split('x')]
    dimensions.sort()
    length, width, height = dimensions
    ribbon = 2 * (length + width) + length * width * height
    part2Result += ribbon
    
print("Part 2: " + str(part2Result))
