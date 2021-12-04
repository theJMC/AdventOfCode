BITLEN = 12
filedata = []


def regen_filedata():
    global filedata
    filedata = [line.rstrip() for line in open('/Users/jamesmccarthy/Library/Mobile Documents/com~apple~CloudDocs/Documents/Code/AdventOfCode/Day3/input.txt')]

def mostOccurO2(bit):
    global totals
    bitList = [item[bit] for item in filedata]
    print(bitList)
    num0s = bitList.count('0') 
    num1s = bitList.count('1')
    return 0 if num0s > num1s else 1

def mostOccurCO2(bit):
    global totals
    if len(filedata) == 1:
        return filedata[0][bit]
    bitList = [item[bit] for item in filedata]
    print(bitList)
    num0s = bitList.count('0') 
    num1s = bitList.count('1')
    return 0 if num0s <= num1s else 1

def removeBlanks(list):
    return [value for value in list if value != '-']


def main():
    global filedata

    # O2
    for bit in range(BITLEN):
        most = mostOccurO2(bit)
        i = 0
        for i in range(len(filedata)):
            if str(filedata[i])[bit] != str(most):
                filedata[i] = '--'
        filedata = [i for i in filedata if i != "--"]
    print(filedata)
    o2val = filedata[0]

    regen_filedata()
    # CO2
    for bit in range(BITLEN):
        most = mostOccurCO2(bit)
        i = 0
        for i in range(len(filedata)):
            if str(filedata[i])[bit] != str(most):
                filedata[i] = '--'
        filedata = [i for i in filedata if i != "--"]
    print(filedata)

    co2val = filedata[0]

    print(int(o2val,2) * int(co2val,2))
            

if __name__ == "__main__":
    regen_filedata()
    main()

