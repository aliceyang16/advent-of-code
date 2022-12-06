import copy

def readfile(filename):
    content = []
    with open(filename) as input:
        for line in input:
            reading = list(line.replace("\n", ""))
            content.append(reading)

    return content

def binaryToDecimal(binary):
    return int(binary, 2)

def listToString(list):
    string = ""
    for letter in list:
        string += letter
    return string

def getGammaEpsilon(content):
    total_readings = len(content)
    records = [0] * len(content[0])
    for reading in content:
        for i in range(len(reading)):
            if int(reading[i]) == 1:
                records[i] += 1

    binary_gamma = ""
    binary_epsilon = ""
    for record in records:
        if record > (total_readings/2):
            binary_gamma += "1"
            binary_epsilon += "0"
        else:
            binary_gamma += "0"
            binary_epsilon += "1"


    gamma = binaryToDecimal(binary_gamma)
    epsilon = binaryToDecimal(binary_epsilon)

    return (gamma, epsilon)

def getRecords(content):
    records = [0] * len(content[0])
    for reading in content:
        for i in range(len(reading)):
            if int(reading[i]) == 1:
                records[i] += 1
    return records

def getCommonLeastValues(length, records, type):
    common = []
    least = []
    for record in records:
        if record >= (length/2):
            common.append(1)
            least.append(0)
        else:
            common.append(0)
            least.append(1)

    if type == "oxygen":
        return common
    else:
        return least


def getOxygenScrubber(content, type):
    results = copy.deepcopy(content)
    reading_size = len(content[0])

    for i in range(reading_size):
        records = getRecords(results)
        criteria = getCommonLeastValues(len(results), records, type)
        results_temp = copy.deepcopy(results)
        for result in results:
            if len(results) > 1:
                if int(result[i]) != criteria[i]:
                    results_temp.remove(result)
                    results = copy.deepcopy(results_temp)
            else:
                return results[0]
    return results[0]


if __name__ == "__main__":
    filename = "input.txt"
    content = readfile(filename)
    gamma, epsilon = getGammaEpsilon(content)
    oxygen_list = getOxygenScrubber(content, "oxygen")
    scrubber_list = getOxygenScrubber(content, "scrubber")
    oxygen = binaryToDecimal(listToString(oxygen_list))
    scrubber = binaryToDecimal(listToString(scrubber_list))
    ans = oxygen * scrubber
    print(ans)