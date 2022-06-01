def connectedComponent(graph):
	noOfComponents = 0
	visited = set()
	
	for src in graph:
		if src not in visited:
			DFS(graph, src, visited)
			noOfComponents += 1

	return noOfComponents

def DFS(graph, src, visited):
	graphStack = [ src ]
	if src not in visited: visited.add(src)

	while len(graphStack) != 0:
		current = graphStack.pop()

		for neighbor in graph[current]:
			if neighbor not in visited:
				graphStack.append(neighbor)
				visited.add(neighbor)

	return True

g = {
	0: [0,1,5],
	1: [0],
	5: [0,8],
	8: [0,5],
	2: [3,4],
	3: [2,4],
	4: [3,2]
}
print(connectedComponent(g))