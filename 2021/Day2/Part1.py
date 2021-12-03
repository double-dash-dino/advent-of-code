# Get the input data

with open('2021/Day2/input-day-2.txt') as f:
    input_lines = f.readlines()

# Clean the data

directions = []
for line in input_lines:
    clean_line = line.replace("\n", "")
    directions.append(clean_line)

# Iterate through the directions adding or subtracting to the direction / depth accordingly

depth = 0
distance = 0
for direction in directions:
    if direction[0] == "f":
        distance += int(direction[-1])
    elif direction[0] == "d":
        depth += int(direction[-1])
    else:
        depth -= int(direction[-1])

print(depth*distance)
    