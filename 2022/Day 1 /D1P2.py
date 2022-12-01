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
    num1 = max(elfTotals)
    elfTotals.remove(num1)
    num2 = max(elfTotals)
    elfTotals.remove(num2)
    num3 = max(elfTotals)
    print(num1 + num2 + num3)