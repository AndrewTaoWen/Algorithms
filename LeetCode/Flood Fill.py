image = [[0, 0, 0], [0, 1, 0]]
sr = 1
sc = 1
newColor = 2


# image = [[0,0,0],[0,0,0]],
# sr = 0
# sc = 0
# newColor = 2

def floodFill(image, sr, sc, newColor):
    memo = {}

    def neighbour(e):
        if e in memo:
            return memo[e]

        yMax = len(image)
        xMax = len(image[0])

        n = []

        if e[1] - 1 >= 0:
            n.append((e[0], e[1] - 1))
        if e[1] + 1 < xMax:
            n.append((e[0], e[1] + 1))
        if e[0] + 1 < yMax:
            n.append((e[0] + 1, e[1]))
        if e[0] - 1 >= 0:
            n.append((e[0] - 1, e[1]))

        memo[e] = n

        return n

    q = [(sr, sc)]
    visited = set()
    visited.add((sr, sc))

    colour = image[sr][sc]

    while q:
        exploring = q.pop(0)
        if image[exploring[0]][exploring[1]] == colour:
            image[exploring[0]][exploring[1]] = newColor
        neighbours = neighbour(exploring)
        print(neighbours)
        for i in neighbours:
            # print(i[0],i[1])
            if image[i[0]][i[1]] == colour:
                print(i[0], i[1])
                image[i[0]][i[1]] = newColor
                # print(image)
                if i not in visited:
                    q.append(i)

            visited.add(i)

    print(image)


floodFill(image, sr, sc, newColor)

