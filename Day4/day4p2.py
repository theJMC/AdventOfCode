totalNumOfBoards = 3


def file_input():
    with open("Day4/testinput.txt") as f:
        order = f.readline().rstrip().split(",")
        #order[-1] = order[-1].rstrip()

        boards = []
        while True:
            f.readline()
            currentBoard = []
            for _ in range(5):
                currentBoard.append(f.readline().rstrip().split())
            if currentBoard == [[] for i in range(5)]:
                return order, boards
            else:
                boards.append(currentBoard)


def checkBoard(board):
    for row in board:
        if row.count("-") >= 5:
            return True
    
    for col in range(5):
        numOfWins = 0
        for row in range(5):
            if board[row][col] == "-":
                numOfWins += 1
        if numOfWins >= 5:
            return True
    
    return False

def checkNum(board, target):
    for row in range(0,5):
        for col in range(0,5):
            if board[row][col] == str(target):
                board[row][col] = "-"
    return board


def boardRecursive(boards, index, target):
    totalWins = 0
    checkNum(boards[index], target)
    popped_board = ""
    if checkBoard(boards[index]):
        totalWins += 1
        popped_board = boards.pop(index)
    if totalWins >= totalNumOfBoards:
        return popped_board, target, boards
    return boardRecursive(boards)

def boardSequence(boards, num, index):
    totalWins = 0
    checkNum(boards[index], num)
    popped_board = "-"
    if checkBoard(boards[index]):
        totalWins += 1
        popped_board = boards.pop(index)
    if totalWins >= totalNumOfBoards:
        pass
    if popped_board == "-":
        return boards[index], num, boards
    else:
        return popped_board, num, boards


def main():
    order, boards = file_input()
    
    for numIndex in range(len(order)):
        num = order[numIndex]
        index = 0
        while True:
            if index >= len(boards):
                break
            if len(boards) > 1:
                _, num, boards = boardRecursive(boards, num, index)
            elif len(boards) <= 1:
                return boardRecursive(boards, num, index)
            index += 1

    

    

if __name__ == "__main__":
    winningBoard, winningNum, boards = main()
    score = 0
    for row in range(len(winningBoard)):
        for col in range(len(winningBoard[row])):
            if winningBoard[row][col] != "-":
                score += int(winningBoard[row][col])   
    print(f"boards: {boards} \nwinningBoard: {winningBoard} \nwinningNum: {winningNum} \nscore: {score}")
    print(int(winningNum) * score)
    