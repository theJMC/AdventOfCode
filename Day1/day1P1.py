

def increasingFunc(list):
    increased = 0
    for i in range(len(list)):
        if i == 0:
            pass
        else:
            if int(list[i]) > int(list[i-1]):
                increased += 1
    return increased

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
        print(increasingFunc(lines))


