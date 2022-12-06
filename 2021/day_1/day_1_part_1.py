filename = "input.txt"

previous = 0
counter = 0
lines = 0
with open(filename) as input:
    while True:
        line = input.readline()
        if not line:
            break

        current = int(line)

        if previous != 0:
            if current > previous:
                counter += 1
        
        previous = current

        lines += 1

print("Counter", counter)
print("Lines", lines)