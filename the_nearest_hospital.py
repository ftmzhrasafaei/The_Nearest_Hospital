import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        # Nodes can get added to the priority queue multiple times. We only process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def MatToDic(mat):
    dic = {}
    for i in range(len(mat)):
        key = str(i)
        value = {}
        for k in range(len(mat[i])):
            if mat[i][k] == 1:
                value[str(k)] = 1
        dic[key] = value
    return dic




f = open("graph.txt", "r")
N = int(f.readline())
hospitalNodes = [int(i) for i in (f.readline()).split()]
graph = []
for j in range(N):
    graph.append([int(i) for i in (f.readline()).split()])



d = MatToDic(graph)


distances = [calculate_distances(d, str(hos)) for hos in hospitalNodes]

result = ''
for i in range(len(graph)):
    m = []
    for distance in distances:
        m.append(distance[str(i)])
    result = result  + str(min(m))
print(result)
