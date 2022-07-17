
def file_input():
    with open("Day4/input.txt") as f:
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
    for row in range(5):
        for col in range(5):
            if board[row][col] == str(target):
                board[row][col] = "-"
    return board


def main():
    order, boards = file_input()
    
    for num in order:
        for i in range(len(boards)):
            checkNum(boards[i], num)
            if checkBoard(boards[i]):
                return boards[i], num
    

if __name__ == "__main__":
    winningBoard, winningNum = main()
    score = 0
    for row in range(len(winningBoard)):
        for col in range(len(winningBoard[row])):
            if winningBoard[row][col] != "-":
                score += int(winningBoard[row][col])   
    print(int(winningNum) * score)
    