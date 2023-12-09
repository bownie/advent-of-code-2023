from collections import Counter
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")
args = parser.parse_args()

CARD_MAPPING = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}


def get_type(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 6
    if len(counts) == 2:
        if 4 in counts.values():
            return 5
        if 3 in counts.values() and 2 in counts.values():
            return 4
    if len(counts) == 3:
        if 3 in counts.values() and list(counts.values()).count(1) == 2:
            return 3
        if list(counts.values()).count(2) == 2:
            return 2
    if len(counts) == 4:
        return 1
    return 0


def get_order(hand):
    return [CARD_MAPPING.get(card, card) for card in hand]


def sorting(hand):
    return get_type(hand), get_order(hand)


plays = []
with open(args.filename, 'r', encoding="utf-8") as file:
    data = file.read().split("\n")
    for line in data:
        hand, bid = line.split()
        plays.append((hand, int(bid)))

plays.sort(key=lambda play: sorting(play[0]))

ans = 0
for rank, (hand, bid) in enumerate(plays, 1):
    ans += bid * rank

print(ans)