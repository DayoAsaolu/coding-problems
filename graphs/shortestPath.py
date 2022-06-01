def shortest_path(edges, nodeA, nodeB):
	graph = build_graph(edges)
	visited = set()
	graphQueue = [ [nodeA, 0 ] ] 
	if nodeA not in visited: visited.add(nodeA)

	while len(graphQueue) != 0:
		current = graphQueue.pop(0)
		if current[0] == nodeB: return current[1]
		 
		for neighbor in graph[current[0]]:
			if neighbor not in visited:
				srcDist = current[1] +1
				graphQueue.append( [ neighbor, srcDist ] )
				visited.add(neighbor)
	
	return -1



def build_graph(edges):
	graph = {}
	
	for edge in edges:
		i , j = edge
		if i not in graph:
			graph[i] = [j]
		else:
			graph[i].append(j)

		if j not in graph:
			graph[j] = [i]
		else:
			graph[j].append(i)
	
	return graph


edges = [
	['w','x'],
	['x','y'],
	['z','y'],
	['z','v'],
	['w','v']
]

print(shortest_path(edges, 'w', 'z'))