def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

temp_seeds, *rest = read_file("input1.txt").split("\n\n")
temp_seeds = list(map(lambda x: int(x), temp_seeds.split(":")[1].split()))
seeds = []
for i in range(0, len(temp_seeds)-1, 2):
    seeds.append((temp_seeds[i], temp_seeds[i] + temp_seeds[i+1]))


for part in rest: 
    intervals = [] 
    for l in part.split("\n")[1:]:
        intervals.append(list(map(lambda x: int(x), l.split())))
    new_seeds=[]
    while seeds:
        start, end = seeds.pop()
        for start_desc, start_source, increment in intervals:
            if start > start_source: 
                overlap_start = start
            else:
                overlap_start = start_source
            if end < start_source + increment:  
                overlap_end = end
            else:
                overlap_end = start_source + increment
            if overlap_start < overlap_end:
                new_seeds.append((overlap_start - start_source + start_desc, overlap_end - start_source + start_desc))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if overlap_end < end:
                    seeds.append((overlap_end, end))
                break
        else:
            new_seeds.append((start, end))
    seeds = new_seeds

min = seeds[0][0]
for x, _ in seeds:
    if x < min:
        min = x

print(min)
# print(len(seeds))