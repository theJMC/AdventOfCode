with open("input.txt") as f:
    data = f.readlines()
    elfTotals = []
    tempArr = []
    for line in data:
        if line.strip() == "":
            elfTotals.append(sum(tempArr))
            tempArr = []
        else:
            tempArr.append(int(line.strip()))
    print(max(elfTotals))