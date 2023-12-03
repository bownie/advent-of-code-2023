import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")

args = parser.parse_args()

partMap = []
specialCharMap = []
numberMap = []

for line in open(args.filename, 'r', encoding="utf-8"):
    line = line.strip()
    partMap.append(line)
    print(f"append {line}")

print(f"partMap length = {len(partMap)}")
# locate all the number blocks
for y in range(len(partMap)):
    startNumberPos: int = -1
    for x in range(len(partMap[0])):
        #print(f"Line {y}")
        if not partMap[y][x].isnumeric():
            if partMap[y][x] != ".":
                print(f"Found {partMap[y][x]} at {x},{y}")
                specialCharMap.append((x,y))

            if startNumberPos != -1:
                insertNumber = ""
                for b in range(x - startNumberPos):
                    insertNumber += partMap[y][startNumberPos + b]
                numberMap.append((startNumberPos, y, insertNumber))
                print(f"completed number at {startNumberPos},{x} on line {y}")
                startNumberPos = -1
        else:
            if startNumberPos == -1:
                startNumberPos = x
            

total: int = 0
# locate all number blocks

for pN in numberMap:
    print(f"pN = {pN}")
    
    pX = int(pN[0])
    pY = int(pN[1])
    pValue = int(pN[2])

    # is there a special symbol within one
    for sC in specialCharMap:
        sX = int(sC[0])
        sY = int(sC[1])

        print(f"sC = {sC}")

        # within 1 y
        if sY >= pY - 1 and sY <= pY + 1 and sX >= pX -1 and sX <= pX + len(pN[2]):
            total +=  pValue


print(f"Total = {total}")