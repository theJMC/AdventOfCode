
def process(target):
    count = 0
    for line in target:
        elf1 = line.strip().split(',')[0].split('-')
        elf2 = line.strip().split(',')[1].split('-')

        elf1Set = set(range(int(elf1[0]), int(elf1[1]) + 1))
        elf2Set = set(range(int(elf2[0]), int(elf2[1]) + 1))
        
        if len(elf1Set.intersection(elf2Set)) > 0:
            count += 1
        elif len(elf2Set.intersection(elf1Set)) > 0:
            count += 1
    return count
    

def main():
    with open("input.txt", 'r') as f:
        data = f.readlines()
        print(process(data))

def test():
    data = ["4-5,2-8"]
    print(process(data))

main()