def BFS(graph, src):
    visted = set()
    graphQueue = [ src ]

    if src not in visted: visted.add(src)

    while len(graphQueue) != 0:
        current = graphQueue.pop(0)
        print(current)

        for neighboor in graph[current]:
            if neighboor not in visted:
                visted.add(neighboor)
                graphQueue.append(neighboor)

    return 0

def DFS(graph, src):
    visted = set()
    graphStack = [ src ]

    if src not in visted: visted.add(src)

    while len(graphStack) != 0:
        current = graphStack.pop()
        print(current)

        for neighboor in graph[current]:
            if neighboor not in visted:
                visted.add(neighboor)
                graphStack.append(neighboor)

    return 0

g = {
    'i':['j','k'],
    'j':['i'],
    'k':['i','m','l'],
    'm':['k'],
    'l':['k']
}

DFS(g, 'i')