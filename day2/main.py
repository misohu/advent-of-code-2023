
FILENAME1="input1A.txt"
RULES1 = {'red': 12, 'green': 13, 'blue': 14}

def parse_input(input_text):
    games = {}
    for line in input_text.strip().split('\n'):
        parts = line.split(':')
        game_number = int(parts[0].strip().split()[1])
        rounds = parts[1].split(';')

        game_data = []
        for round_data in rounds:
            colors = {'red': 0, 'green': 0, 'blue': 0}
            for item in round_data.split(','):
                count, color = item.strip().split()
                colors[color] += int(count)
            game_data.append(colors)

        games[game_number] = game_data

    return games

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

def play_game(file_name, rule):
    content = read_file(file_name)
    inputs = parse_input(content)
    result = 0
    print (inputs)
    for index, games in inputs.items():
        lost = False
        for game in games:
            for color, value in rule.items():
                if value < game[color]:
                    lost = True
                    continue
        if lost:
            continue
        result += index
    return result
        
def play_game2(file_name):
    content = read_file(file_name)
    inputs = parse_input(content)
    result = 0

    for _, games in inputs.items():
        maxes = {'red': 0, 'green': 0, 'blue': 0}
        for game in games:
            for color, value in game.items():
                if value > maxes[color]:
                    if value == 0:
                        continue
                    maxes[color] = value
        tmp = 1
        for v in maxes.values():
            tmp *=v
        result += tmp
        
    return result

if __name__ == "__main__":
    print(play_game2(FILENAME1))