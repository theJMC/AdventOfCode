def getData():
    #with open("input.txt", "r") as file:
    with open("/Users/jamesmccarthy/Library/Mobile Documents/com~apple~CloudDocs/Documents/Code/AdventOfCode/Day3/falseinput.txt", "r") as file:
        lines = [line.rstrip('\n') for line in file]

        fdata = [[],[],[],[],[],[],[],[],[],[],[],[]]

        for i in range(5):
            for line in lines:
                fdata[i].append(line[i])
    return fdata, lines

def generate(list):
    zero = 0
    one = 0
    for i in list:
        if int(i) == 0:
            zero += 1
        else:
            one += 1
    return (zero, one)

def oxy_y(raw, val, bit, item):
    print(f"test: {str(raw[item - 1])} test2: {len(raw)}, test3: {item}")
    condition = str(raw[item - 1])
    if condition[bit] == str(val):
        #print(f"rawpop {raw.pop(item - 1)}")
        raw.pop(item - 1)

def oxy(gen_data, raw, bit):
    if gen_data[bit][0] > gen_data[bit][1]:
        val = 0
    else:
        val = 1
    for item in range(len(raw)):
        if len(raw) > item-1:
            oxy_y(raw, val, bit, item)
    if len(raw) == 1:
        return

def co2(gen_data, raw, bit):
    if gen_data[bit][0] < gen_data[bit][1]:
        val = 0
    else:
        val = 1
    for item in range(len(raw)):
        if len(raw) > item-1:
            oxy_y(raw, val, bit, item)
    if len(raw) == 1:
        return

def main():
    gen_data, raw = prep()

    # Oxy Rating
    
    for bit in range(len(raw[0])):
        oxy(gen_data, raw, bit)
    print(raw)

    gen_data, raw = prep()
    for bit in range(len(raw[0])):
        co2(gen_data, raw, bit)
    print(raw)


def prep():
    data, raw = getData()
    gen_data = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(data)):
        gen_data[i] = generate(data[i])
    print(gen_data)
    return gen_data, raw


if __name__ == "__main__":
    main()