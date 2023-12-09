# https://github.com/xHyroM/aoc/blob/main/2023/8/second.py

import re
import math
import argparse, re
from functools import reduce
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")
args = parser.parse_args()
file = open(args.filename).readlines()

instructions = list(file[0].strip())
nodes = {
    x[1]: (x[2], x[3])
    for x in (re.match(r"(\w+)\s*=\s*\((\w+), (\w+)\)", line) for line in file[2:])
}

count = []

for next_node in [n for n in nodes if n.endswith("A")]:
    steps = 0
    i = 0

    while not next_node.endswith("Z"):
        if i >= len(instructions):
            i = 0

        instruction = instructions[i]
        cur_node = nodes[next_node]
        next_node = cur_node[instruction == "R"]

        steps += 1
        i += 1

    count.append(steps)

print(math.lcm(*count))