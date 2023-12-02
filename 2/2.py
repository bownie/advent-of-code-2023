import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")
parser.add_argument("red", help="red cubes")
parser.add_argument("green", help="green cubes")
parser.add_argument("blue", help="blue cubes")

args = parser.parse_args()

mapNumbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

totalRed: int = int(args.red)
totalGreen: int = int(args.green)
totalBlue: int = int(args.blue)


print(f"Total Red = {totalRed}")
print(f"Total Green = {totalGreen}")
print(f"Total Blue = {totalBlue}")

finalScore: int = 0
part2FinalScore: int = 0

for line in open(args.filename, 'r', encoding="utf-8"):
    line = line.strip()

    game_details=line.split(":")
    gameNumber: int = int(game_details[0].split(" ")[1])
    game_draw=game_details[1]

    #print(f"gameNumber = {gameNumber}")

    possible: bool = True

    # part 2
    countRed = 0
    countGreen = 0
    countBlue = 0

    for draw in game_draw.split(";"):
        for colour in draw.split(","):
            draw_details = colour.strip().split(" ")
            cubeCount: int = int(draw_details[0])
            cubeColour = draw_details[1]

            #print(f"Game {gameNumber} {cubeColour} = {cubeCount}")
            match cubeColour:
                case "red":                        
                    if cubeCount > totalRed:
                        #print(f"RED OVER {cubeCount} {totalRed}")
                        possible = False

                    if cubeCount > countRed:
                        countRed = cubeCount

                case "green":
                    if cubeCount > totalGreen:
                        #print(f"GREEN OVER {cubeCount} {totalGreen}")
                        possible = False

                    if cubeCount > countGreen:
                        countGreen = cubeCount

                case "blue":
                    if cubeCount > totalBlue:
                        #print(f"BLUE OVER {cubeCount} {totalBlue}")
                        possible = False

                    if cubeCount > countBlue:
                        countBlue = cubeCount

    if possible:
        finalScore += gameNumber

    part2FinalScore += countRed * countGreen * countBlue

    

print(f"Total for part 1 = {finalScore}")


print(f"Total for part 2 = {part2FinalScore}")