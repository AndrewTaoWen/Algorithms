
vertices, edges = input().split()

vertices = int(vertices)
edges = int(edges)

g = [[] for i in range(vertice s +1)]

for i in range(edges):
    v1, v2, weight = input().split()
    v1 = int(v1)
    v2 = int(v2)
    weight = int(weight)
    g[v1].append((v2 ,weight))
    g[v2].append((v1 ,weight))

dist = [float('inf')] * (vertice s +1)
dist[1] = 0
q = [1]
visited = set()

while q:
    curV = q.pop(0)
    if curV in visited:
        continue

    for nbr in g[curV]:
        # print(nbr)
        if nbr[0] in visited:
            continue

        newDist = dist[curV] + nbr[1]
        # print(newDist)
        if dist[nbr[0]] > newDist:
            dist[nbr[0]] = newDist
            q.append(nbr[0])

    visited.add(curV)

for i in range(vertice s +1):
    if i == 0:
        pass
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])
