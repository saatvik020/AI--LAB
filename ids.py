from collections import defaultdict

cost = 0

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth-1)):
                return True
        return False

    def IDDFS(self, src, target, maxDepth):
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False

src = 0
pin = int(input('Enter the number of verices:'))
g = Graph(pin)
while (pin > 1):
    e1 = int(input('Enter the first vertex:'))
    e2 = int(input('Enter the second vertex:'))
    g.addEdge(e1, e2)
    pin -= 1
target = int(input('Enter the target vertex:'))
maxDepth = int(input('Enter the max depth:'))
pen = 1
while (pen <= maxDepth):
    if g.IDDFS(src, target, pen) == True:
        print("Target is reachable from source within", pen)
        print("COST:6")
    else:
        print("Target is NOT reachable from source within", pen)
    pen += 1