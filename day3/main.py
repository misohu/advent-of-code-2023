def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

content = read_file("input1.txt")
symbol_positions = set()
field = content.split('\n')

for x, row in enumerate(field):
    for y, column in enumerate(row):
        if column.isdigit() or column == '.':
            continue
        symbol_positions.add((x,y))

number_beginnings = set()
for x,y in symbol_positions: 
    for tx in range(x-1, x+2):
        for ty in range(y-1, y+2):
            if tx < 0 or tx > len(field) or not field[tx][ty].isdigit():
                continue
            if ty < 0 or ty > len(field[tx]) or not field[tx][ty].isdigit():
                continue
            while ty > 0 and field[tx][ty - 1].isdigit():
                ty -= 1
            number_beginnings.add((tx,ty))

numbers = []
for x,y in number_beginnings:
    temp = ""
    while y < len(field[x]) and field[x][y].isdigit():
        temp += field[x][y]
        y+=1
    numbers.append(int(temp))

print(sum(numbers))
