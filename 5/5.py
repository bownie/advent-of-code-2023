import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")

args = parser.parse_args()

total: int = 0

seeds = []
transformMap = {}
mapName = ""

part2 = True

for line in open(args.filename, 'r', encoding="utf-8"):
    line = line.strip()
    if line.split(":")[0] == "seeds":
        seeds = line.split(":")[1].strip().split(" ")
    else:
        if line.find(":") > 0:
            mapName = line.split(":")[0].split(" ")[0].strip()
            #print(f"FOUND mapName = {mapName}")
            transformMap[mapName] = []
        else:
            tuple=line.strip().split(" ")

            # only use a valid numeric list
            if len(tuple) > 0 and tuple[0].isnumeric():
                #print(f"Numbers = {tuple}")
                transformMap[mapName].append(tuple)

def transformInput(seed: int, tuple: []) -> int:
    target=int(tuple[0])
    source=int(tuple[1])
    transform_range=int(tuple[2])

    #print(f"tuple = {tuple}")
    if seed >= source and seed <= source + transform_range:
        #print(f"transformed {seed} to {seed + target - source}")
        return seed + target - source
    return seed


location = []

# step through seeds
for seed in seeds:
    print(f"Transforming seed {seed}")
    seed = int(seed)

    transformed=-1
    for map in transformMap.keys():
        for tuple in transformMap[map]:
            transformed = transformInput(int(seed), tuple)
            if transformed != seed:
                seed = transformed
                break

        print (f"{map} transform = {transformed}")

    location.append(transformed)



#print(f"seeds = {seeds}")
#print(f"mapCount = {len(transformMap)}")
#print(f"total = {total}")
print(f"lowest location = {min(location)}")