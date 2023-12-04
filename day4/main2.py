from collections import defaultdict

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

content = read_file("input1.txt")

cards = content.splitlines()
result = 0
counter = defaultdict(int)

for card in cards:
    tmp = card.split(":")
    card_number = int(tmp[0].split()[1])
    counter[card_number] += 1
    all_numbers = tmp[1]
    numbers = all_numbers.split("|")
    winning_numbers = numbers[0].split()
    your_numbers = numbers[1].split()

    copies = 0 
    for number in your_numbers:
        if number in winning_numbers:
            copies+=1
    for i in range(1, copies+1):
        counter[card_number + i] += counter[card_number]
    
print(sum(counter.values()))
