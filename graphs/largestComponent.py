def largestcomponent(graph):
	visited = set()
	largestComponent = 0

	for src in graph:
		if src not in visited:
			size = DFS(graph, src, visited)
			if size > largestComponent:
				largestComponent = size

	
	return largestComponent


def DFS(graph, src, visited):
	size = 0
	graphStack = [ src ]
	if src not in visited: visited.add(src)
	
	while len(graphStack) != 0:
		current = graphStack.pop()
		size+= 1
		for neighbor in graph[current]:
			if neighbor not in visited:
				graphStack.append(neighbor)
				visited.add(neighbor)

	return size

graph = {
	0: [0,1,5],
	1: [0],
	5: [0,8],
	8: [0,5],
	2: [3,4],
	3: [2,4],
	4: [3,2]
}
print(largestcomponent(graph))