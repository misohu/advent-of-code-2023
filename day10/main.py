from collections import deque

map_grid = open("input.txt", "r").read().splitlines()


visited = set()
queue = deque()

for x, line in enumerate(map_grid):
    for y, c in enumerate(line):
        if c == "S":
            visited.add((x,y))
            queue.append((x,y))

while queue:
    x, y = queue.popleft()
    c = map_grid[x][y]

    if x > 0:
        next = map_grid[x - 1][y]
        if (x-1, y) not in visited:    
            if c in "S|JL" and next in "|7F":
                visited.add((x-1,y))
                queue.append((x-1,y))
    
    if x < len(map_grid) - 1:
        next = map_grid[x + 1][y]
        if (x+1, y) not  in visited:
            if c in "S|7F" and next in "|JL":
                visited.add((x+1,y))
                queue.append((x+1,y))

    
    if y > 0:
        next = map_grid[x][y -1]
        if (x, y-1) not in visited:
            if c in "S-J7" and next in "-LF":
                visited.add((x,y-1))
                queue.append((x,y-1))
    
    if y < len(map_grid[x]) - 1:
        next = map_grid[x][y+1]
        if (x, y+1) not in visited:
            if c in "S-LF" and next in "-J7":
                visited.add((x,y+1))
                queue.append((x,y+1))

print(len(visited) // 2)