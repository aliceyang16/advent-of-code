import numpy as np


def readfile(filename):
    reading = []
    x_values = []
    y_values = []
    with open(filename) as input:
        for line in input:
            point_1, point_2 = line.replace("->", "").split()
            x1, y1 = point_1.split(",")
            x2, y2 = point_2.split(",")
            first = (int(x1), int(y1))
            second = (int(x2), int(y2))
            reading.append([first, second])
            x_values.append(int(x1))
            x_values.append(int(x2))
            y_values.append(int(y1))
            y_values.append(int(y2))

    return reading, max(x_values) + 1, max(y_values) + 1


def getStartEndValues(value1, value2):
    if value1 > value2:
        return (value2, value1 + 1)
    else:
        return (value1, value2 + 1)


def getStartEndPoints(point1, point2):
    if point1[0] > point2[0]:
        return (point2, point1)
    else:
        return (point1, point2)


def isDiagonal(first, second):
    if abs(first[0] - second[0]) == abs(first[1] - second[1]):
        return True
    else:
        return False


def mapVents(vents, x_size, y_size):
    grid = np.zeros([y_size, x_size], dtype=int)

    for line in vents:
        point1 = line[0]
        point2 = line[1]
        # x points the same
        if point1[0] == point2[0]:
            start, end = getStartEndValues(point1[1], point2[1])
            for y in range(start, end):
                grid[y, point1[0]] += 1
        # y points the same
        elif point1[1] == point2[1]:
            start, end = getStartEndValues(point1[0], point2[0])
            for x in range(start, end):
                grid[point1[1], x] += 1
        else:
            if isDiagonal(point1, point2):
                start_point, end_point = getStartEndPoints(point1, point2)
                start_x, end_x = getStartEndValues(start_point[0], end_point[0])

                y_diff = end_point[1] - start_point[1]
                print("start_end", (start_point, end_point))
                y = start_point[1]
                for x in range(start_x, end_x):
                    print("xy", (x, y))
                    grid[y, x] += 1
                    y += np.sign(y_diff)

    return grid


def countMap(grid):
    freq = grid > 1
    return freq.sum()


if __name__ == "__main__":
    filename = "input.txt"
    vents, x_size, y_size = readfile(filename)
    grid = mapVents(vents, x_size, y_size)
    print(grid)
    freq = countMap(grid)
    print(freq)
