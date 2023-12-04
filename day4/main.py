def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

content = read_file("input1.txt")
cards = content.splitlines()
result = 0

for card in cards:
    all_numbers = card.split(":")[1]
    numbers = all_numbers.split("|")
    winning_numbers = numbers[0].split()
    your_numbers = numbers[1].split()
    print(winning_numbers, your_numbers)

    points = 0 
    for number in your_numbers:
        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *=2
    result+=points
    print(points)

print(result)
