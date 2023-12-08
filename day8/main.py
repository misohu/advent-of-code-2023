input_map = {}

file_input = open("input.txt", "r").read().splitlines()
directions = file_input[0]

for line in file_input[2:]:
    parts = line.split("=")
    sides = parts[1].split(",")
    node = parts[0].strip()
    input_map[node] = {
        "L": sides[0][2:5],
        "R": sides[1][:-1].strip()
    }

pos = 0
current = "AAA"
while current != "ZZZ":
    current = input_map[current][directions[pos % len(directions)]]
    pos +=1

print(pos)