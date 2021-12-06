TEST = True
DAYS = 3


class Fish:
    def __init__(self, daysUntil=9):
        self.daysUntil = daysUntil

    def __repr__(self):
        return str(self.daysUntil)

    def increment(self):
        if self.daysUntil == 0:
            self.daysUntil = 6
            return True
        self.daysUntil -= 1



def getData():
    if TEST:
        return [3,4,3,1,2]
    else:
        with open('Day6/input.txt', 'r') as f:
            return f.readline().rstrip().split(",")
"""
def iterate(possibilities):
    temp = possibilities[0]
    for i in range(len(possibilities)-1):
        possibilities[i] = possibilities[i+1]
    if temp == 0:
        possibilities[-1] = temp
    else:
        possibilities[6] += temp
        possibilities[8] += temp
    return possibilities

if __name__ == "__main__":
    data = getData()
    possibilities = [0 for _ in range(9)]
    print(possibilities)
    for i in range(len(data)):
        possibilities[data[i]] += 1

    for i in range(DAYS):
        possibilities = iterate(possibilities)

    print(possibilities)
    print(sum(possibilities))"""

def nicePrint(dict):
    for key in dict:
        print(f"{key} : {dict[key]}")

if __name__ == "__main__":
    data = getData()
    numbersDict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }

    for i in range(len(data)):
        numbersDict[data[i]] += 1

    for i in range(DAYS):
        for key in numbersDict:
            if numbersDict[0] == 0:
                numbersDict[-1] = 0
            else:
                temp = numbersDict[0]
            
                

    nicePrint(numbersDict)









    