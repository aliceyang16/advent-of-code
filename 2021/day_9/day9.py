import numpy as np


def readfile(filename):
    readings = []
    with open(filename) as input:
        for line in input:
            reading = line.replace("\n", "")
            processed = [int(i) for i in reading]
            readings.append(processed)

    return np.matrix(np.array(readings))


def windowMatrix(matrix):
    min_columns = []
    rows, columns = matrix.shape
    for i in range(columns):
        min_value = int(min(matrix[:, i]))
        j = int(np.where(np.array(matrix[:, i]) == min_value)[0])
        # (x, y, value)
        min_columns.append((j, i, min_value))
    return (rows, columns, min_columns)


def findMin(rows, columns, collection):
    for row in range(rows):
        for col in range(columns):
            if row == 0 and col == 0:
                


if __name__ == "__main__":
    filename = "sample.txt"
    matrix = readfile(filename)
    print(matrix)
    rows, columns, collection = windowMatrix(matrix)
    print(collection)
    # findMin(rows, columns, collection)
