# Index in array is the priority value
priority = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

with open("input.txt",'r') as f:
    data = f.readlines()
    for index in range(len(data)//3):
        bp1 = data[index*3]
        bp2 = data[index*3+1]
        bp3 = data[index*3+2]

        for item in bp1:
            if item in bp2 and item in bp3:
                total += priority.index(item)
                break
        

print(total)