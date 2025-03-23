import os

# Get the directory of this script and join it with "input.txt"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    data = f.read()
    
# Solve part 1 of the problem
houses = set()
houses.add((0, 0))
x = 0
y = 0
for char in data:
    if char == '>':
        x += 1
    elif char == '<':
        x -= 1
    elif char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    houses.add((x, y))

# Print the number of unique houses visited
print("Part 1: " + str(len(houses)))

santaHouses = set()
santaHouses.add((0, 0))
roboHouses = set()
roboHouses.add((0, 0))

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0

for i, char in enumerate(data):
    if i % 2 == 0:
        if char == '>':
            santa_x += 1
        elif char == '<':
            santa_x -= 1
        elif char == '^':
            santa_y += 1
        elif char == 'v':
            santa_y -= 1
        santaHouses.add((santa_x, santa_y))
    else:
        if char == '>':
            robo_x += 1
        elif char == '<':
            robo_x -= 1
        elif char == '^':
            robo_y += 1
        elif char == 'v':
            robo_y -= 1
        roboHouses.add((robo_x, robo_y))
        
# Combine the two sets of houses to get the total number of unique houses visited
total_houses = santaHouses.union(roboHouses)
print("Part 2: " + str(len(total_houses)))