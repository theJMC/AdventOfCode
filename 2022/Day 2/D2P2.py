with open("input.txt", "r") as f:
    total = 0
    """
    for i in range(1):
        data = f.readline()"""
    data = f.readlines()
    for match in data:
        play, result = match.strip().split(" ")
        print(f"Play: {play}, Result: {result}")
        match result:
            case "X":
                print("Loose")
                # Loose
                match play:
                    case "A": # Rock
                        choice = "Scissors"
                    case "B": # Paper
                        choice = "Rock"
                    case "C": # Scissors
                        choice = "Paper"
            case "Y":
                print("Tie")
                # Tie
                match play:
                    case "A": # Rock
                        choice = "Rock"
                    case "B": # Paper
                        choice = "Paper"
                    case "C": # Scissors
                        choice = "Scissors"
            case "Z":
                # Win
                match play:
                    case "A": # Rock
                        choice = "Paper"
                    case "B": # Paper
                        choice = "Scissors"
                    case "C": # Scissors
                        choice = "Rock"
        total += {"Rock": 1, "Paper": 2, "Scissors": 3}[choice]
        total += {"X": 0, "Y": 3, "Z": 6}[result]

print(total)


