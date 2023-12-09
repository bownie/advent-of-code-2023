import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename")

args = parser.parse_args()

total: int = 0

seed_ranges = []
transformMap = {}
mapName = ""

for line in open(args.filename, 'r', encoding="utf-8"):
    line = line.strip()
    if line.split(":")[0] == "seeds":

        all_seed_ranges = line.split(":")[1].strip().split(" ")
        for i in range(int(len(all_seed_ranges)/2)):
            print(f"adding range {i}  - start number = {all_seed_ranges[i * 2]}, range = {all_seed_ranges[1+ i * 2]}")
            seed_ranges.append([int(all_seed_ranges[i * 2]), int(all_seed_ranges[1+ i * 2])])

        print(f"Seed tuples = {seed_ranges}")
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

# we're transforming ranges here so we might end up with more ranges
def transformInput(seed_range: [int, int], tuple: []) -> int:
    target=int(tuple[0])
    source=int(tuple[1])
    transform_range=int(tuple[2])

    seed_base=seed_range[0]
    seed_range=seed_range[1]

    print(f"seed_base = {seed_base}")
    print(f"seed_range = {seed_range}")
    if seed_base >= source and seed_base + seed_range <= source + transform_range:
        #print(f"transformed {seed} to {seed + target - source}")
        return seed_base + target - source
    return seed


location = []

# step through seeds
for seed_range in seed_ranges:
    print(f"Transforming seed range {seed_range}")

    transformed=-1
    for map in transformMap.keys():
        for tuple in transformMap[map]:
            transformed = transformInput(seed_range, tuple)
            if transformed != seed:
                seed = transformed
                break

 #       print (f"{map} transform = {transformed}")#

  #  location.append(transformed)



#print(f"seeds = {seeds}")
#print(f"mapCount = {len(transformMap)}")
#print(f"total = {total}")
#print(f"lowest location = {min(location)}")
