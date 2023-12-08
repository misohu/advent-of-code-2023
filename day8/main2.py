from math import gcd

input_map = {}

file_input = open("input.txt", "r").read().splitlines()
directions = file_input[0]
currents = []

for line in file_input[2:]:
    parts = line.split("=")
    sides = parts[1].split(",")
    node = parts[0].strip()
    input_map[node] = {
        "L": sides[0][2:5],
        "R": sides[1][:-1].strip()
    }
    if node.endswith("A"):
        currents.append(node)


loops = []
for current in currents:
    loop = []

    counter = 0
    first_goal = None
    while True:
        while counter == 0 or not current.endswith("Z"):
            current = input_map[current][directions[counter % len(directions)]]
            counter +=1
        loop.append(counter)
        if not first_goal:
            first_goal = current
            counter = 0
        elif current == first_goal:
            break
    loops.append(loop)

loops = [loop[0] for loop in loops]
lcm = 1
for i in loops:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)