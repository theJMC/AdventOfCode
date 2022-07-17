TEST = False
TARGET = None

from statistics import median

def getData():
    if TEST:
        return [16,1,2,0,4,2,7,1,2,14]
    else:
        with open("Day7/input.txt") as f:
            return [int(x) for x in f.readline().rstrip().split(",")]

def getCost(crab, target):
    dist = abs(crab-target)
    print(f"Crab needs to get from {crab} to {target} -> Dist {dist}")
    return dist

if __name__ == "__main__":
    data = getData()
    target = int(median(data)) if TARGET == None else TARGET

    maxVal = max(data)
    minVal = min(data)
    print(f"Max Val = {max(data)}")

    fuelCost = 0

    totalsDict = {}

    for i in range(minVal, maxVal + 1):
        fuelCost = 0
        for crab in data:
            fuelCost += getCost(crab, i)
        totalsDict[i] = fuelCost
        pass

    minFuel = min(totalsDict.values())
    print(minFuel)
        
    ivd = {v: k for k, v in totalsDict.items()}
    
    mostEfficient = ivd[min(totalsDict.values())]
    print(mostEfficient)

    
