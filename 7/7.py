import argparse
from functools import reduce
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")
args = parser.parse_args()

total: int = 0
cardValues = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
orderedList = {}

def sortHand(hand: str) -> []:
    sortedValue = [0] * len(cardValues)
    for card in hand:
        print(f"Card = {card}, Score={cardValues.index(card)}")
        sortedValue[cardValues.index(card)] += 1

    return sortedValue

def scoreHand(sortedHand: []):
    score = 0
    print("sorted hand:")
    for i in range(len(sortedHand)):
        print(f"{len(sortedHand) - i} = {sortedHand[i]}")
        addScore = 0
        if (sortedHand[i] > 0):
            addScore = pow((len(sortedHand) - i), sortedHand[i])
        print(f"pos {i}, addScore = {addScore}")
        score += addScore
        print(f"pos {i}, totalScore = {score}")
    return score

def insertHand(hand: str, bet: str, score: int):
    orderedList[score] = [hand, bet]


for line in open(args.filename, 'r', encoding="utf-8"):
    line = line.strip()

    hand=line.split(" ")[0]
    bet=line.split(" ")[1]

    sortedHand = sortHand(hand)
    score=scoreHand(sortedHand)

    print(f"Hand = {hand}, score = {score}")

    insertHand(hand, bet, score)


for score in sorted(orderedList.keys()):
    print(f"{score}")

##    for i in range(len(sortedHand)):
  #      print(f"{i} = {sortedHand[i]}")



#    if len(orderedList) == 0:
#        orderedList.append([hand, bet])
#    else:
 #       valueHand(hand, bet)
