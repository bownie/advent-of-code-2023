import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")

args = parser.parse_args()

winning_numbers = []
my_guesses = []
total: int = 0

total_lines = 0

line_copies = {}

# initialize line_copies
for i in range(200):
    line_copies[i] = 1

#def get_number_of_wins():

for line in open(args.filename, 'r', encoding="utf-8"):
    numbers=line.split(":")[1].strip()

    #print(f"numbers={numbers}")

    # the split and strip is getting empty values into number and guess which 
    # is very annoying - not quite sure why at this point
    #
    for number in numbers.split("|")[0].strip().split(" "):
        if (number.isnumeric()):
            winning_numbers.append(int(number))

    for guess in numbers.split("|")[1].strip().split(" "):
        if (guess.isnumeric()):
            my_guesses.append(int(guess))

    line_total = 0
    for guess in my_guesses:
        if guess in winning_numbers:
            line_total += 1

    original_amount = line_copies[total_lines]
    # increment
    for i in range(line_total):
        line_copies[1 + i + total_lines] += original_amount

    winning_numbers.clear()
    my_guesses.clear()

    total_lines += 1

# sum up
for i in range(total_lines):
    print(f"line {i} = {line_copies[i]}")
    total += line_copies[i]

print(f"total = {total}")
