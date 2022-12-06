def readfile(filename):
    outputs = []
    inputs = []
    with open(filename) as input:
        for line in input:
            reading = line.split()
            output = reading[-4:]
            input = reading[:-5]
            outputs.append(output)
            inputs.append(input)
    return (inputs, outputs)


def countUniqueNumbers(outputs):
    counter = 0
    for output in outputs:
        length = len(output)
        if (length == 7) or (length == 3) or (length == 4) or (length == 2):
            counter += 1
    print("Counter", counter)


def getUniqueMap(inputs):
    map = {}
    for input in inputs:
        length = len(input)
        sorted_input = sorted(input)
        string_input = "".join(sorted_input)
        if length == 2:
            map[1] = string_input
        elif length == 4:
            map[4] = string_input
        elif length == 3:
            map[7] = string_input
        elif length == 7:
            map[8] = string_input
    return map


def checkLetters(sub, input):
    for c in sub:
        if c not in input:
            return False
    return True


def specialLettersCheck(sub, input):
    counter = 0
    for c in sub:
        if c in input:
            counter += 1

    if counter == 3:
        return True

    return False


def mapLength5Number(input, map):
    if checkLetters(map[7], input):
        map[3] = input
    elif specialLettersCheck(map[4], input):
        map[5] = input
    else:
        map[2] = input


def mapLength6Number(input, map):
    if checkLetters(map[4], input):
        map[9] = input
    elif checkLetters(map[1], input):
        map[0] = input
    else:
        map[6] = input


def getMap(inputs, map):
    for input in inputs:
        length = len(input)
        sorted_input = sorted(input)
        string_input = "".join(sorted_input)
        if length == 5:
            mapLength5Number(string_input, map)
        if length == 6:
            mapLength6Number(string_input, map)


def getKey(val, map):
    for key, value in list(map.items()):
        if val == value:
            return key
    return "Key does not exist"


def decodeOutput(outputs, map):
    number = ""
    for output in outputs:
        sorted_output = sorted(output)
        string_output = "".join(sorted_output)
        number += str(getKey(string_output, map))

    print(number)
    return int(number)


if __name__ == "__main__":
    filename = "8"
    inputs, outputs = readfile(filename)
    sum = 0
    for i in range(len(inputs)):
        # for i in range(len(inputs) - 1, len(inputs)):
        map = getUniqueMap(inputs[i])
        getMap(inputs[i], map)
        print(map)
        # decodeOutput(outputs[i], map)
        sum += decodeOutput(outputs[i], map)
    # countUniqueNumbers(outputs)
    print(sum)
