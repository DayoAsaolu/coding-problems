def topSort(graph):
    visited = set()
    topSorted = []

    for node in graph:
        if node not in visited:
            order = DFS(graph,node,visited)
            topSorted += order[0]
    return topSorted[::-1]


def DFS(graph, src, visited):
    graphStack = [ src ]
    order = []

    if src not in visited: visited.add(src)

    while len(graphStack) != 0:
        current = graphStack.pop()
        order.append(current)

        for neighboor in graph[current]:
            if neighboor not in visited:
                graphStack.append(neighboor)
                visited.add(neighboor)

    return [order, visited]


def main():
    graph = {
        0: [1, 2],
        1: [2, 5],
        2: [3],
        3: [],
        4: [],
        5: [3, 4],
        6: [1, 5],
    }

    graph1 = {
        'e': ['d'],
   'a': [],
   'b': ['a'],
   'c': ['a'],
   'd': ['b', 'c'],
   
}


    print("topSort-->", topSort(graph1))
    return 0


main()