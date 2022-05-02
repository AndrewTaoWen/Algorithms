arr = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]


def unique(arr):
    newlist = []
    for i in arr:
        if i not in newlist:
            newlist.append(i)

    return newlist


print(unique(arr))

# n = int(input())
# l = []

# for i in range(1,n):
#     if i % 2 == 0:
#         l.append(i)

# print(set(l))