import argparse, re
from operator import add
from functools import reduce
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")
args = parser.parse_args()
file = open(args.filename).readlines()      

def diff_list(values):
    rV = []
    for i in range(len(values) - 1):
        rV.append(values[i + 1] - values[i])
    return rV

def get_next_value(all_array):
    rV = 0
    for x in range(len(all_array)):
        rV += int(all_array[len(all_array) - 1 - x])

    return rV

for line in file:
    values = list(map(int, line.strip().split(" ")))
    
    check_list = []
    last_list = values

    while reduce(add, last_list) > 0:
        last_list = diff_list(last_list)
        check_list.append(last_list)

        print(f"result = {get_next_value(last_list)}")


    print(f"check_list = {check_list}")
    print(f"line = {values}")

