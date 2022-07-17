TEST = False
DAYS = 256

validTimers = [x for x in range(0, 9)]

def getData():
    if TEST:
        return [3,4,3,1,2]
    else:
        with open('Day6/input.txt', 'r') as f:
            list = f.readline().rstrip().split(",")
            return [int(x) for x in list]


def sim(fishDict):
    for day in range(DAYS):
        print(f"Day {day}")
        spawnReset = fishDict[0]
        for timer in validTimers:
            match timer:
                case 8:
                    fishDict[timer] = spawnReset
                case 6:
                    fishDict[timer] = fishDict[timer + 1] + spawnReset
                case _:
                    fishDict[timer] = fishDict[timer + 1]
    return fishDict

if __name__ == "__main__":
    data = getData()
    fishDict = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0
    }

    # Get data into dict
    for item in data:
        fishDict[item] += 1

    fishDict = sim(fishDict)
    print(sum(fishDict.values()))









    