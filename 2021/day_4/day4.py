import copy


def readfile(filename):
    bingo_boards = []
    bingo_board = []
    with open(filename) as input:
        bingo_seq = input.readline().split(",")
        for line in input:
            if line != "\n":
                bingo_board.append(line.split())
            else:
                if len(bingo_board) > 0:
                    bingo_boards.append(bingo_board)
                    bingo_board = []

        if len(bingo_board) > 0:
            bingo_boards.append(bingo_board)

    return (bingo_seq, bingo_boards)


def getInitialMarkedBoard(length):
    marked_boards = []
    row = [0] * 5
    column = [0] * 5
    for i in range(length):
        board = [row, column]
        marked_boards.append(board)
    return marked_boards


def markBingoBoard(bingo_board, number):
    for row in range(5):
        for column in range(5):
            if bingo_board[row][column] == number:
                bingo_board[row][column] = None
                break


def checkRowColumn(bingo_board):
    for i in range(5):
        row = list(filter(None, bingo_board[i][:]))
        column_temp = [bingo_board[j][i] for j in range(5)]
        column = list(filter(None, column_temp))

        if (len(row) == 0) or (len(column) == 0):
            print("BINGO")
            return True
    return False


def checkBingoWinner(bingo_seq, bingo_boards):
    for number in bingo_seq:
        for i in range(len(bingo_boards)):
            markBingoBoard(bingo_boards[i], number)
            isBingo = checkRowColumn(bingo_boards[i])
            if isBingo:
                return (bingo_boards[i], number)


def checkLastBingoWinner(bingo_seq, bingo_boards):
    total_boards = len(bingo_boards)
    removed_boards = []
    all_boards = [i for i in range(total_boards)]
    for number in bingo_seq:
        for board in bingo_boards:
            markBingoBoard(board, number)
            isBingo = checkRowColumn(board)
            if isBingo:
                removed_boards.append(bingo_boards.index(board))

            if total_boards - len(removed_boards) == 0:
                remaining = list(set(all_boards) - set(removed_boards))
                return bingo_boards[remaining[0]], number


def checkNumberLeadingToBingo(bingo_seq, board, number):
    start_index = bingo_seq.index(number)
    for i in range(start_index, len(bingo_seq)):
        markBingoBoard(board, bingo_seq[i])
        isBingo = checkRowColumn(board)
        if isBingo:
            return bingo_seq[i]


def convertToInt(bingo_board):
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] is not None:
                bingo_board[i][j] = int(bingo_board[i][j])


def sumWinnerBoard(bingo_board, number):
    sum = 0
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] is not None:
                sum += int(bingo_board[i][j])
    return sum * int(number)


if __name__ == "__main__":
    filename = "input.txt"
    bingo_seq, bingo_boards = readfile(filename)
    last_winner, number = checkLastBingoWinner(bingo_seq, bingo_boards)
    number = checkNumberLeadingToBingo(bingo_seq, last_winner, number)
    # winner_board, number = checkBingoWinner(bingo_seq, bingo_boards)
    # score = sumWinnerBoard(winner_board, number)
    print(number)
    score = sumWinnerBoard(last_winner, number)
    print(score)
