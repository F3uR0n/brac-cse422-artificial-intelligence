import heapq

# Input File
def read_file(filename):
    graph = {}
    heuristic = {}
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()

            if not parts:
                continue
            
            city = parts[0]
            heuristic[city] = int(parts[1])
            graph[city] = []

            for i in range(2, len(parts), 2):
                neigh = parts[i]
                neighDistance = int(parts[i+1])
                graph[city].append(neigh, neighDistance)

# A*
def aStar (start, goal, graph, heuristic):
    visited = set()

    gScore = {node: float('inf') for node in graph}
    gScore[start] = 0

    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    parent = {start: None}

    while pq:
        pass