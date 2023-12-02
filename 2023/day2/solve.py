import sys
sys.path.insert(0, '.')
from util.read_input import read_input

# input = read_input("day2/sample")
input = read_input("day2/input")

# part 1
def part_one_solution():
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0
    for game in input:
        game_number = game.split(":")[0].replace("Game", "")
        draws = game.split(":")[1].split(";")

        isValid = True
        for draw in draws:
            values = draw.split(",")
            for value in values:
                number = value.split(" ")[1]
                color = value.split(" ")[2]

                if int(number) > cubes[color]:
                    isValid = False

        if isValid:
            sum += int(game_number)

    print("Part one answer: ", sum)

def part_two_solution():
    answer = 0
    for game in input:
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game_number = game.split(":")[0].replace("Game", "")
        draws = game.split(":")[1].split(";")

        isValid = True
        for draw in draws:
            values = draw.split(",")
            for value in values:
                number = value.split(" ")[1]
                color = value.split(" ")[2]

                cubes[color] = max(cubes[color], int(number))
        game_product = cubes["red"] * cubes["blue"] * cubes["green"]
        answer += game_product
    print("Part two answer: ", answer)


if __name__ == "__main__":
    part_one_solution()
    part_two_solution()
