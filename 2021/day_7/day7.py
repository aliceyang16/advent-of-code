import collections


def readfile(filename):
    readings = open(filename).read().split(",")
    content = [int(i) for i in readings]
    return content


def getFreq(crabs):
    collection = collections.Counter(crabs)
    common = collection.most_common()
    return common


def getFuelCost(crabs, common):
    fuelCosts = []
    for freq in common:
        fuelCost = 0
        for pos in crabs:
            fuelCost += abs(pos - freq[0])
        fuelCosts.append(fuelCost)
    print(fuelCosts)
    return min(fuelCosts)


def getMoreFreq(crabs):
    max_pos = max(crabs)
    collect = []
    for i in range(max_pos + 1):
        collect.append((i, crabs.count(i)))
    return collect


def steppedFuel(number):
    stepped = 0
    for i in range(number):
        stepped += i
    return stepped


def getSteppedFuel(crabs, common):
    fuelCosts = []
    for freq in common:
        fuelCost = 0
        for pos in crabs:
            diff = abs(pos - freq[0])
            step = steppedFuel(diff)
            fuelCost += diff + step
        fuelCosts.append(fuelCost)
    print(fuelCosts)
    return min(fuelCosts)


if __name__ == "__main__":
    filename = "input.txt"
    crabs = readfile(filename)
    freq = getMoreFreq(crabs)
    fuelCost = getSteppedFuel(crabs, freq)
    print(fuelCost)
