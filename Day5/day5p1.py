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

def x_equal(line):
    return True if int(line[0][0]) == int(line[1][0]) else False

def y_equal(line):
    return True if int(line[0][1]) == int(line[1][1]) else False

def populateGraph(lines, graph):
    acceptableLines = []
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            acceptableLines.append(line)
    
    print(acceptableLines)

    points = []

    for index, line in enumerate(acceptableLines):
        if x_equal(line):
            x = line[0][0]
            for y in range(int(line[0][1]), int(line[1][1])):
                points.append((x, y))
        elif y_equal(line):
            y = line[0][1]
            for x in range(int(line[0][0]), int(line[1][0])):
                points.append((x, y))
    
    return graph, points

if __name__ == "__main__":
    graph = createGraph()
    print(graph)
    lines = getLines()
    graph, points = populateGraph(lines, graph)
    
    for item in points:
        print(points)

    for i in range(len(graph)-1, 0, -1):
        print(graph[i])