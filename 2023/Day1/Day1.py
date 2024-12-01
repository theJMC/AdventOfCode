
class Day1:
    def __init__(self):
        with open("input.txt") as f:
            self.input = f.read().splitlines()
            self.digitsDict = {
                'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9
            }

    def Part1(self):
        result = []
        for line in self.input:
            first = None
            last = None
            for char in line:
                if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if first is None:
                        first = char
                    last = char
            result.append(int(str(first) + str(last)))
        return sum(result)

    def Part2(self):
        result = []
        for line in self.input:
            first = None
            last = None
            for 

            for char in line:
                if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if first is None:
                        first = char
                    last = char
                    continue
            result.append(int(str(first) + str(last)))
        return sum(result)


if __name__ == "__main__":
    day = Day1()
    print(day.Part2())
