def readfile(filename):
    content = []
    with open(filename) as input:
        for line in input:
            direction, step = line.split()
            instruction = {direction: int(step)}
            content.append(instruction)

    return content

def getPosition(content):
    horizontal = 0
    depth = 0
    for instruction in content:
        direction = list(instruction.keys())[0]
        if direction == "forward":
            horizontal += instruction[direction]
        elif direction == "up":
            depth -= instruction[direction]
        elif direction == "down":
            depth += instruction[direction]

    return (horizontal, depth)

def getComplicatedPosition(content):
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in content:
        direction = list(instruction.keys())[0]
        if direction == "forward":
            horizontal += instruction[direction]
            depth += aim * instruction[direction]
        elif direction == "up":
            aim -= instruction[direction]
        elif direction == "down":
            aim += instruction[direction]

    return (horizontal, depth)

if __name__ == "__main__":
    filename = "input.txt"
    content = readfile(filename)
    horizontal, depth = getComplicatedPosition(content)
    ans = horizontal * depth
    print(ans)
