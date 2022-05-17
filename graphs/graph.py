def depthfirtsearch(src, graph):
    graphStack = [ src ]

    while len(graphStack) != 0:
        current = graphStack.pop()
        print(current)

        for neighboor in graph[current]:
            graphStack.append(neighboor)

    return 0


def breathfirstsearch( src, graph):
    graphQueue = [ src ]

    while len(graphQueue) != 0:
        current = graphQueue.pop(0)
        print(current)

        for neighboor in graph[current]:
            graphQueue.append(neighboor)


    return 0

g = {
    "a":["c", "b"],
    "b":["d", "e"],
    "c":["f"],
    "d":[],
    "e":[],
    "h":["d"],
    "f":[]
}

# depthfirtsearch("a", g)
breathfirstsearch("a", g)