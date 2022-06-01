def depthfirtsearch(src, graph):
    graphStack = [ src ]

    while len(graphStack) != 0:
        current = graphStack.pop()
        print(current)

        for neighboor in graph[current]:
            graphStack.append(neighboor)

    return 0

def recursiveDFS(graph, src):
    print(src)

    for neighboor in graph[src]:
        recursiveDFS(graph, neighboor)

    return 0

def breathfirstsearch( src, graph):
    graphQueue = [ src ]

    while len(graphQueue) != 0:
        current = graphQueue.pop(0)
        print(current)

        for neighboor in graph[current]:
            graphQueue.append(neighboor)

    return 0

def converToAdjacent(edges):
    graph = {}

    for i in edges:
        x, y = i


        if x not in graph: 
            graph[x] = [y]
        else: 
            graph[x].append(y)
        
        if y not in graph:
            graph[y] = [x]
        else:
            graph[y].append(x)

    return graph


def hasPathDFS(graph, src, des):
    graphQueue = [ src ]

    while len(graphQueue) != 0:
        current = graphQueue.pop(0)
        if current == des:
            return True
        for neighboor in graph[current]:
            graphQueue.append(neighboor)

        
    return -1

def hasPathBFS(graph, src, des):
    graphQueue = [ src ]

    while len(graphQueue) != 0:
        current = graphQueue.pop()
        if current == des:
            return True
        for neighboor in graph[current]:
            graphQueue.append(neighboor)
        
    return -1

g = {
    "a":["c", "b"],
    "b":["d", "e"],
    "c":["f"],
    "d":[],
    "e":[],
    "h":["d"],
    "f":[]
}

edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]

path = {
    'f': ['g', 'i'],
    'g': ['h'],
    'i': ['g', 'k'],
    'h': [],
    'j': ['i'],
    'k': []
}

numbers = {
    1: [2,4],
    2: [3],
    3: [],
    4: [3]
}
# depthfirtsearch("a", g)
# breathfirstsearch("a", g)
# print(converToAdjacent(edges))

# print(hasPathBFS(path,'f','k'))
recursiveDFS(numbers, 1)
