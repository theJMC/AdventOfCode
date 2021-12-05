DIMENSIONS = 9
FILE = 'Day5/testinput.txt'

def createGraph():
    graph = [[0 for _ in range(DIMENSIONS)] for _ in range(DIMENSIONS)]
    return graph

def getLines():
    lines = []
    with open(FILE) as f:
        for line in f:
            splitLine = line.rstrip().split(" -> ")
            bothSplit = (splitLine[0].split(","), splitLine[1].split(","))
            lines.append(bothSplit)
    return lines

def populateGraph(lines, graph):
    acceptableLines = []
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            acceptableLines.append(line)
    
    print(acceptableLines)

    for index, line in enumerate(acceptableLines):
        if line[0][0] == line[1][0]:
            for y in range(int(line[0][1]), int(line[1][1])):
                # print(f"{y} , {line[0][0]}")
                graph[y][int(line[0][1])] += 1
        elif line[0][1] == line[1][1]:
            for x in range(int(line[0][0]), int(line[1][0])):
                # print(f"{x} , {line[0][1]}")
                graph[int(line[0][0])][x] += 1
    
    return graph

             

    
if __name__ == "__main__":
    graph = createGraph()
    print(graph)
    lines = getLines()
    graph = populateGraph(lines, graph)
    
    for i in range(len(graph)-1, 0, -1):
        print(graph[i])