# filename = "input.txt"

# counter = 0
# lines = 0

# with open(filename) as input:
#     A = int(input.readline())
#     B = int(input.readline())
#     C = int(input.readline())
#     sum_prev = A + B + C
#     while True:
#         line = input.readline()
#         if not line:
#             break

#         A = int(line)
#         sum_curr = A + B + C
#         if sum_curr > sum_prev:
#             counter += 1

#         B = A
#         C = B

#         sum_prev = sum_curr

#         lines += 1

# print("Counter", counter)
# print("Lines", lines)

def getCounter(content):
    counter = 0
    sum_prev = int(content[0]) + int(content[1]) + int(content[2])
    for i in range(3, len(content)):
        sum_curr = int(content[i]) + int(content[i-1]) + int(content[i-2])
        if sum_curr > sum_prev:
            counter += 1

        sum_prev = sum_curr

    return counter

if __name__ == "__main__":
    filename = "input.txt"
    print("Hello World")
    content = open(filename).read().split("\n")
    new_content = content[:len(content)-1]
    ans = getCounter(new_content)
    print(ans)
