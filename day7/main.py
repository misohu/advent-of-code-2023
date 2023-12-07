from dataclasses import dataclass
from typing import List
from collections import defaultdict 

card_value_mapping = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E'
}

@dataclass
class Hand:
    cards: str
    value: int
    type: int=-1

def find_type(hand: Hand):
    counts = [hand.cards.count(card) for card in hand.cards]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


with open("input1.txt", "r") as file:
    content = file.read()

hands = []
for line in content.splitlines():
    tmp = line.split()
    hand=Hand(
        cards= ''.join(card_value_mapping.get(char, char) for char in tmp[0]),
        value=int(tmp[1])
    ) 
    hand.type =  find_type(hand) 
    hands.append(hand)

hands.sort(key=lambda hand: (hand.type, hand.cards))

result = 0

for rank, hand in enumerate(hands, 1):
    result += rank * hand.value

print(result)

