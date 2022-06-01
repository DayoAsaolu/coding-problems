path = {
    'f': ['g', 'i'],
    'g': ['h'],
    'i': ['g', 'k'],
    'h': [],
    'j': ['i'],
    'k': []
}

def hasPath(graph, src, des):

    if src == des: return True
    graphQueue = [ src ]

    while len(graphQueue) != 0:
        current = graphQueue.pop()
        if current == des: return True

        for neighbour in graph[current]:
            graphQueue.append(neighbour)

    return -1 

def hasPathRec(graph, src, dst):
    if src == dst: return True

    for neigbhoor in graph[src]:
        if hasPathRec(graph, neigbhoor, dst): return True

    return -1


print(hasPathRec(path, 'f', 'h'))

# print(hasPath(path, 'f', 'j'))