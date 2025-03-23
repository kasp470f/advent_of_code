import os

# Get the directory of this script and join it with "input.txt"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    data = f.read()
    
# Solve part 1 of the problem
lights = [[0] * 1000 for _ in range(1000)]
for line in data.splitlines():
    words = line.split()
    command = None
    start = None
    end = None
    if len(words) == 5:
        command = f"{words[0]} {words[1]}"
        start = words[2].split(',')
        end = words[4].split(',')
    else:
        command = words[0]
        start = words[1].split(',')
        end = words[3].split(',')
        
    start = (int(start[0]), int(start[1]))
    end = (int(end[0]), int(end[1]))
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if command == "toggle":
                lights[i][j] = 1 - lights[i][j]
            elif command == "turn on":
                lights[i][j] = 1
            elif command == "turn off":
                lights[i][j] = 0
                
# Count the number of lights that are on
print(f"Part 1: {sum(sum(row) for row in lights)}")
    
    
# Solve part 2 of the problem
lights = [[0] * 1000 for _ in range(1000)]
                
for line in data.splitlines():
    words = line.split()
    command = None
    start = None
    end = None
    if len(words) == 5:
        command = f"{words[0]} {words[1]}"
        start = words[2].split(',')
        end = words[4].split(',')
    else:
        command = words[0]
        start = words[1].split(',')
        end = words[3].split(',')
        
    start = (int(start[0]), int(start[1]))
    end = (int(end[0]), int(end[1]))
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if command == "toggle":
                lights[i][j] += 2
            elif command == "turn on":
                lights[i][j] += 1
            elif command == "turn off":
                lights[i][j] -= 1 if lights[i][j] > 0 else 0
                
print(f"Part 2: {sum(sum(row) for row in lights)}")