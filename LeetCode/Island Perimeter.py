grid = [[1,0]]

maxY = len(grid)-1
maxX = len(grid[0])-1

# memo = {}

def neighbours(v):
    # if v in memo:
    #     return memo[v]

    n = []

    y = v[0]
    x = v[1]

    if y+1 <= maxY:
        n.append((y+1,x))
    if x+1 <= maxX:
        n.append((y,x+1))

            # memo[v] = n

    return n

q = [(0,0)]

cnt = 0

visited = set()
visited.add((0,0))

while q:
    exploring = q.pop(0)
            # print(neighbour)

    for i in neighbours(exploring):
            a = grid[i[0]][i[1]]
            b = grid[exploring[0]][exploring[1]]
            if a == 1 and b == 0:
                    cnt += 1
            elif a == 0 and b == 1:
                    cnt += 1
            if i not in visited:
                    q.append(i)
                    visited.add(i)

    if grid[exploring[0]][exploring[1]] == 1:
            if exploring[0] == 0:
                    cnt += 1
            if exploring[1] == maxX:
                    cnt += 1
            if exploring[1] == 0:
                    cnt += 1
            if exploring[0] == maxY:
                    cnt += 1

print(cnt)