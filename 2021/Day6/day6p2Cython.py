TEST = False
DAYS = 256


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
        with open('input.txt', 'r') as f:
            return f.readline().rstrip().split(",")


if __name__ == "__main__":
    data = getData()
    fish = []
    for d in data:
        fish.append(Fish(daysUntil = int(d)))

    for i in range(DAYS):
        print(f"day {i}")
        for f in fish:
            if f.increment():
                fish.append(Fish())

    print(len(fish))
    #print(fish)
