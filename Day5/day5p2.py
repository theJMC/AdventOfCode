DIMENSIONS = 1000
FILE = 'Day5/input.txt'

def createGraph():
    graph = [[0 for _ in range(DIMENSIONS)] for _ in range(DIMENSIONS)]
    return graph

def getLines():
    lines = []
    with open(FILE) as f:
        for line in f:
            splitLine = line.rstrip().split(" -> ")
            split1 = [int(item) for item in splitLine[0].split(",")]
            split2 = [int(item) for item in splitLine[1].split(",")]
            bothSplit = (split1, split2)
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
        print(f"working on line: {line}")
        x1 = line[0][0]
        x2 = line[1][0]
        y1 = line[0][1]
        y2 = line[1][1]
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                print(f"appended point: {(x, y)}")
                points.append((x, y))

    for item in points:
        graph[item[1]][item[0]] += 1
    
    return graph, points

if __name__ == "__main__":
    graph = createGraph()
    lines = getLines()
    graph, points = populateGraph(lines, graph)

    numOfgreaterThanOne = 0

    for i in range(len(graph)):
        #print(graph[i])
        for j in range(len(graph[i])):
            if graph[i][j] > 1:
                numOfgreaterThanOne += 1

    print(f"score: {numOfgreaterThanOne}")

