import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")

args = parser.parse_args()

winning_numbers = []
my_guesses = []
total: int = 0

for line in open(args.filename, 'r', encoding="utf-8"):
    numbers=line.split(":")[1].strip()

    print(f"numbers={numbers}")

    # the split and strip is getting empty values into number and guess which 
    # is very annoying - not quite sure why at this point
    #
    for number in numbers.split("|")[0].strip().split(" "):
        if (number.isnumeric()):
            winning_numbers.append(int(number))

    for guess in numbers.split("|")[1].strip().split(" "):
        if (guess.isnumeric()):
            my_guesses.append(int(guess))

    print(f"winning_numbers = {winning_numbers}")
    print(f"my_guesses = {my_guesses}")
    line_total = 0

    for guess in my_guesses:
        if guess in winning_numbers:
            if line_total == 0:
                line_total = 1
            else:
                line_total *= 2

    total += line_total

    winning_numbers.clear()
    my_guesses.clear()

print(f"total = {total}")
