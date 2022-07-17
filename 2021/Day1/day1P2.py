from day1P1 import increasingFunc

with open("input.txt", "r") as file:
    lines = file.readlines()

    newlines = []
    for item in lines:
        newlines.append(item.rstrip())
    windows = []
    for i in range(len(newlines)):
        if i > 2:
            sum = int(newlines[i]) + int(newlines[i-1]) + int(newlines[i-2])
            windows.append(sum)
        
    print(windows)
    print(increasingFunc(windows))
