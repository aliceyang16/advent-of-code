import sys
sys.path.insert(0, '.')
from util.read_input import read_input

# input = read_input("day1/sample")
input = read_input("day1/input")

# Part 1
def part_one_solution():
    answer = 0
    for i in input:
        number = ""
        for n in i:
            if n.isnumeric():
                number += n
        digit = number[0] + number[len(number) - 1]
        answer += int(digit)

    print("Part one answer: ", answer)

# Part 2
def part_two_solution():
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = 0
    for line in input:
        number = ""
        w = 3; i = 0
        while i < len(line):
            if line[i].isnumeric():
                number += line[i]
            else:
                while i+w <= len(line):
                    if line[i:i+w] in numbers:
                        number += numbers[line[i:i+w]]
                    w += 1
                    if w > 5:
                        continue
            i += 1; w = 3
        digit = number[0] + number[len(number) - 1]
        answer += int(digit)

    print("Part two answer: ", answer)

if __name__ == "__main__":
    part_one_solution()
    part_two_solution()