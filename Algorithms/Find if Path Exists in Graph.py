num = 10
edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
start = 7
end = 5


# num = 3
# edges = [[0,1],[1,2],[2,0]]
# start = 0
# end = 2


def validPath(num, start, end, edges):
    def n(e):
        l = []
        for i in edges:
            if i[0] == e:
                l.append(i[1])
            if i[1] == e:
                l.append(i[0])
        return l

    if start == end:
        return True

    visited = set()
    q = [start]
    while q:
        exploring = q.pop(0)
        neighbours = n(exploring)
        print(neighbours)
        for i in neighbours:
            print(i)
            if i == end:
                print(i)
                return True
            if i not in visited:
                visited.add(i)
                q.append(i)

    return False


print(validPath(num, start, end, edges))






