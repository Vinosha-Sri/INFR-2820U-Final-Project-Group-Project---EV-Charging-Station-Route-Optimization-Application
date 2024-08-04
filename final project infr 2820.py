import heapq
# A function is created to convert the array of edges into an adjacency list to implement the algorithm: 
def graphcreation(edges):
    graph = {}
    for start, end, distance in edges:
        if start not in graph:
            graph[start] = {}
        graph[start][end] = distance
    return graph
# Dijkstra's Algorithm is implemented to find the shortest path from the start node to the other nodes: 
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Priority queue is created to see which nodes have the smallest known distance first: 
    priorityqueue = [(0, start)]
    while priorityqueue:
        currentdistance, currentnode = heapq.heappop(priorityqueue)
        # If there is a shorter path to a node, it continue with the next node in the queue: 
        if currentdistance > distances[currentnode]:
            continue
        # Sees the neighbors of the current node: 
        for neighbor, weight in graph[currentnode].items():
            distance = currentdistance + weight
            # If there is a shorter path to the neighbor is found, the distance will be updated and queued: 
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priorityqueue, (distance, neighbor))
    return distances
# Function is created to recommend the nearest charging station based on the distances: 
def recommendedroute(distances, chargingstations):
    neareststation = min(chargingstations, key=lambda station: distances[station])
    return neareststation, distances[neareststation]
if __name__ == "__main__":
    # Array created of edges to represent the graph:
    edges = [
        ('A', 'B', 6), ('A', 'D', 9), ('A', 'F', 14),
        ('B', 'A', 6), ('B', 'C', 10), ('B', 'D', 15),
        ('C', 'B', 10), ('C', 'E', 11),
        ('D', 'A', 9), ('D', 'B', 15), ('D', 'F', 2), ('D', 'E', 6),
        ('E', 'C', 11), ('E', 'D', 6), ('E', 'G', 9),
        ('F', 'A', 14), ('F', 'D', 2), ('F', 'G', 9),
        ('G', 'F', 9), ('G', 'E', 9), ('G', 'H', 1),
        ('H', 'G', 1), ('H', 'I', 7),
        ('I', 'H', 7), ('I', 'J', 8),
        ('J', 'I', 8), ('J', 'K', 10),
        ('K', 'J', 10), ('K', 'L', 11),
        ('L', 'K', 11), ('L', 'M', 8),
        ('M', 'L', 8), ('M', 'N', 9),
        ('N', 'M', 9), ('N', 'O', 6),
        ('O', 'N', 6), ('O', 'P', 6),
        ('P', 'O', 6), ('P', 'Q', 9),
        ('Q', 'P', 9), ('Q', 'R', 10),
        ('R', 'Q', 10), ('R', 'S', 7),
        ('S', 'R', 7), ('S', 'T', 8),
        ('T', 'S', 8), ('T', 'U', 11),
        ('U', 'T', 11), ('U', 'V', 13),
        ('V', 'U', 13), ('V', 'W', 5),
        ('W', 'V', 5)
    ]
    # Converts the array of edges to an adjacency list representation of the graph to do the implementation of the Dijkstra's Algorithm: 
    graph = graphcreation(edges)
    # Prints out the graph representation: 
    print("Graph As An Adjacency List:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    # Start node is stored in a variable:
    startnode = 'A'
    # The shortest distance is calculuated using Dijkstra's Algorithm: 
    distances = dijkstra(graph, startnode)
    print(f"The shortest distances is from {startnode}: {distances}")
    # The charging stations are all stored in a variable: 
    chargingstations = ['H', 'K', 'Q', 'T']
    # Recoommends the nearest charging station based on the distance: 
    neareststation, distance = recommendedroute(distances, chargingstations)
    print(f"The nearest charging station is: {neareststation} at distance {distance}")