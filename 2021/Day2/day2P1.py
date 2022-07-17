

with open("input.txt", "r") as file:
    temp = file.readlines()
    lines = []
    for item in temp:
        lines.append(item.rstrip().split(" "))


    pos = 0
    dep = 0

    for item in lines:
        match item[0]:
            case "forward":
                pos += int(item[1])
            case "down":
                dep += int(item[1])
            case "up":
                dep -= int(item[1])
            case _:
                print(f"ERROR {item[0]}")


    print(f"Position: {pos}")
    print(f"Depth: {dep}")
    print(f"Ans: {pos * dep}")