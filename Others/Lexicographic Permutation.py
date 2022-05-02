permutations = []

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permutations.append([s[0]])

for i in range(1,len(s)):
    # print(i, permutations)
    new_perm = []
    for j in permutations:
        for k in range(len(j)+1):
            # print(j, permutations)
            newJ = j.copy()
            newJ.insert(k,s[i])
            new_perm.append(newJ)
    permutations = new_perm.copy()

# print(permutations)
print(len(permutations))