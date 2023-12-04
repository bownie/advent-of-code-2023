import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")

args = parser.parse_args()

winning_numbers = []
my_guesses = []
total: int = 0

for line in open(args.filename, 'r', encoding="utf-8"):
    numbers=line.split(":")[1].strip()

    number_split=list(numbers.split("|")[0].strip())
    print(f"number_split = {number_split}".strip())

    guess_split=list(numbers.split("|")[1])
    print(f"guess_split = {guess_split}")

    # the split and strip is getting empty values into number and guess which 
    # is very annoying - not quite sure why at this point
    #
    for number in numbers.split("|")[0].strip().split(" "):
        if (number.isnumeric()):
            winning_numbers.append(int(number))

    for guess in numbers.split("|")[1].strip().split(" "):
        if (guess.isnumeric()):
            my_guesses.append(int(guess))

