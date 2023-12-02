def read_input(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    return lines

if __name__ == "__main__":
    print(read_input("./sample"))
