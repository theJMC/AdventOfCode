# Index in array is the priority value
priority = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

with open("input.txt",'r') as f:
    data = f.readlines()
    for backpack in data:
        halfSplitter = len(backpack)//2
        print(halfSplitter)
        half1 = backpack[:halfSplitter]
        half2 = backpack[halfSplitter:]
    
        for item in half1:
            
            if item in half2:

                total += priority.index(item)
                break

print(total)