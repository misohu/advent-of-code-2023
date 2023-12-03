def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

content = read_file("input1.txt")
symbol_positions = set()
field = content.split('\n')
result = 0

for x, row in enumerate(field):
    for y, column in enumerate(row):
        if column != '*':
            continue
        symbol_positions.add((x,y))

for x,y in symbol_positions: 
    number_beginnings = set()
    for tx in range(x-1, x+2):
        for ty in range(y-1, y+2):
            if tx < 0 or tx > len(field) or not field[tx][ty].isdigit():
                continue
            if ty < 0 or ty > len(field[tx]) or not field[tx][ty].isdigit():
                continue
            while ty > 0 and field[tx][ty - 1].isdigit():
                ty -= 1
            number_beginnings.add((tx,ty))
    if len(number_beginnings) == 2:
        numbers = []
        for xx,yy in number_beginnings:
            temp = ""
            while yy < len(field[xx]) and field[xx][yy].isdigit():
                temp += field[xx][yy]
                yy+=1
            numbers.append(int(temp))
        result += (numbers[0] * numbers[1])

print(result)
