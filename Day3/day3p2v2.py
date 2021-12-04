BITNUM = 5
raw = []

def getData():
    global raw
    #with open("input.txt", "r") as file:
    with open("/Users/jamesmccarthy/Library/Mobile Documents/com~apple~CloudDocs/Documents/Code/AdventOfCode/Day3/falseinput.txt", "r") as file:
        raw = [line.rstrip('\n') for line in file]

        fdata = [[] for i in range(BITNUM)]

        for i in range(BITNUM):
            for line in raw:
                fdata[i].append(line[i])

    return fdata


def most_occur(list):
    
    zero = 0
    one = 0
    for i in list:
        if int(i) == 0:
            zero += 1
        else:
            one += 1
    return 0 if zero > one else 1

def prep():
    
    data = getData()
    gen_data = [[] for i in range(BITNUM)]
    for i in range(len(data)):
        gen_data[i] = most_occur(data[i])
    return gen_data

def generate(raw_loc, val, bit):
    
    iter = 0
    pre_len = len(raw_loc)
    #print(len(raw))
    #print(raw)
    done = False
    while not done:
        for item in range(len(raw_loc)):
            iter += 1
            print(f"comparing {str(raw_loc[item])[bit]} to {val} -> {raw_loc[item]}")
            if str(raw_loc[item])[bit] != str(val):
                print(f"Popping {raw_loc.pop(item)}")
                #raw.pop(item)
                break
            if iter >= pre_len:
                done = True
                break
    print(iter)
    

def main():
    getData()
    print(raw)
    # O2
    i = 0
    while i < len(raw):
        print(f"--- NEW BIT CHECK [{i}]---")
        occuring = most_occur(raw[i])
        print(occuring)
        generate(raw, occuring, i)
        i += 1
    print(f"o2val = {raw}")

    o2val = raw[0]

    #gen_data,= prep()
    # C02
    """for i in range(BITNUM):
        print("--- NEW BIT CHECK ---")
        if gen_data[i] == 0:
            val = 1
        else:
            val = 0
        generate(raw, val, i)
    print(raw)"""

    co2val = raw[0]

    o2Int = int(o2val, 2)
    co2Int = int(co2val, 2)

    #print(o2Int * co2Int)



if __name__ == "__main__":
    main()