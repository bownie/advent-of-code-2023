import argparse
from functools import reduce
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")
args = parser.parse_args()

total: int = 0
timeDistance = []
transformMap = {}

holdTime = 0
lineNo = 0
position = 0

for line in open(args.filename, 'r', encoding="utf-8"):
    line = line.strip()


    for fetch in line.split(":")[1].strip().split(" "):
        if (fetch.isnumeric()):
            if lineNo == 0:
                print(f"time = {fetch}")
                timeDistance.append([int(fetch), 0])
            else:
                print(f"distance = {fetch}")
                timeDistance[position][1] = int(fetch)
                position += 1


    lineNo =+ 1


results = []

for timeDist in timeDistance:
    print(f"time = {timeDist[0]}, distance = {timeDist[1]}")

    waysToWin = 0
    for i in range(timeDist[0]):
        distance = i * (timeDist[0] - i)
        if distance > timeDist[1]:
            waysToWin += 1

    results.append(waysToWin)

print(f"total = {reduce(lambda x, y: x*y, results)}")