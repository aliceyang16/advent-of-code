import copy
import collections


def readfile(filename):
    readings = open(filename).read().split(",")
    content = [int(i) for i in readings]
    return content


def addNewFish(tank, number):
    for i in range(number):
        tank.append(8)


def ageFish(initial):
    tank = copy.deepcopy(initial)
    for day in range(1, 257):
        counter = 0
        for i in range(len(tank)):
            if tank[i] > 0:
                tank[i] -= 1
            else:
                tank[i] = 6
                counter += 1
        addNewFish(tank, counter)
        print(f"DAY {day}")
    return tank


def getInitialBins(initial):
    bins = []
    for i in range(9):
        # (age, number of fish)
        bins.append(initial.count(i))
    return bins


def largeFish(initial):
    bins = getInitialBins(initial)
    for day in range(1, 257):
        new_fish = bins[0]
        bins_coll = collections.deque(bins)
        bins_coll.rotate(-1)
        bins = list(bins_coll)
        bins[6] += new_fish

        print(f"Day {day}: {bins}")
    print(sum(bins))
    # return bins


if __name__ == "__main__":
    filename = "input.txt"
    initial = readfile(filename)
    largeFish(initial)
    # print(sum)
    # tank = ageFish(initial)
    # print(len(tank))
