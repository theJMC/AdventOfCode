rpc = {"A": "Rock", "B": "Paper", "C": "Scissors",
        "X": "Rock", "Y": "Paper", "Z": "Scissors"}

optionPoints = {"X": 1, "Y": 2, "Z": 3}
total = 0

def getWinner(p1, p2):
    match rpc[p1]:
        case "Rock":
            match rpc[p2]:
                case "Rock":
                    return "T"
                case "Paper":
                    return "2"
                case "Scissors":
                    return "1"

        case "Paper":
            match rpc[p2]:
                case "Rock":
                    return "1"
                case "Paper":
                    return "T"
                case "Scissors":
                    return "2"

        case "Scissors":
            match rpc[p2]:
                case "Rock":
                    return "2"
                case "Paper":
                    return "1"
                case "Scissors":
                    return "T"

with open("input.txt", "r") as f:
    data = f.readlines()
    for match in data:
        p1, p2 = match.strip().split(" ")
        winner = getWinner(p1, p2)
        if winner == "1":
            roundPoints = 0
        elif winner == "2":
            roundPoints = 6
        else:
            roundPoints = 3
        roundPoints += optionPoints[p2]
        total += roundPoints

print(total)


