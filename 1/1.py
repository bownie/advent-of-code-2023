import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")
args = parser.parse_args()

count: int = 0
mapNumberWords: bool = False

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

for line in open(args.filename, 'r', encoding="utf-8"):
    line = line.strip()

    nums = []
    latestNumberWord: str = ""

    for char in line:            
        if char.isnumeric():
            nums.append(char)
            latestNumberWord: str = "" # reset
        else:
            if (mapNumberWords):
                latestNumberWord += char

                # now we need to reverse build the latest matching numberWord
                i = 0
                findNumber: str = ""
                while i < len(latestNumberWord):
                    findNumber = latestNumberWord[len(latestNumberWord) - i  - 1] + findNumber

                    if findNumber in mapNumbers.keys():
                        i = len(latestNumberWord) + 1
                    else:
                        i += 1
                
                if (i == len(latestNumberWord) + 1):
                    nums.append(mapNumbers[findNumber])
                

    myNum = int(nums[0]) * 10 + int(nums[len(nums) - 1])
    count += myNum
    #print(f"{nums[0]}{nums[len(nums) - 1]}")

print(f"Total = {count}")
