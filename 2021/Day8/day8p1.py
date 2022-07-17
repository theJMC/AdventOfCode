
def getData():
    with open("input.txt") as f:
        output = []
        for line in f.readlines():
            output.append(line.rstrip().split(" | "))
    return output

def getDict():
    numberDict = { 
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg" }

    inverseNumDict = {y: x for x, y in numberDict.items()}
    lengthDict = {x: len(y) for x, y in numberDict.items()}
    return inverseNumDict, lengthDict

def commonWires(wiresDict):
    for item in wiresDict:
        pass

def main():
    data = getData()
    numberDict, lengthDict = getDict()
    vals = []
    for item in data:
        resultVals = { 
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "" }
        for num in item[1].split(" "):
        # for num in data[0][1].split(" "):
            workingDict = dict(numberDict)
            for index, key in enumerate(numberDict):
                if len(key) != len(num):
                    workingDict.pop(key)
            print(workingDict)
            # if len(workingDict) == 1:
            #     for val in workingDict.items():
            #         resultVals[val[1]] = val[0]

        print(resultVals)
                    
                    
    

if __name__ == "__main__":
    main()