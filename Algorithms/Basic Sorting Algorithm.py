# Bubble Sort

# a = list(input())

# while True:
#     count = 0
#     for i in range(0, len(a)-1):

#         b = a[i]
#         c = a[i+1]

#         if b > c:
#             a[i] = c
#             a[i+1] = b
#             count += 1

#     if count == 0:
#         break

# print(a)

# Insertion Sort

a = list(input())

i = 1  # length of sorted sublist, default at 1

while i < len(a):
    j = i
    while i > 0 and a[j - 1] > a[j]:  # while item on left is larger than item on right
        # once the second condition is no longer true, that means the element is in the correct position
        # swap position of the two
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1
    i += 1  # length of sublist increase by 1 each iteration

print(a)

a = list(input())

a_sorted = []

while a:
    smallest = a[0]
    for i in a:
        if i < smallest:
            smallest = i
    a_sorted.append(smallest)
    a.remove(smallest)

print(a_sorted)


# Mr Park Version
def selectSort(array, result=[]):
    if not array:
        return result
    else:
        smallest = array[0]
        small_index = 0

        for i in range(1, len(array)):
            if array[i] < smallest:
                smallest = array[i]
                small_index = i
        # end of for
        result.append(array.pop(small_index))

        return selectSort(array, result)


test = [6, 5, 3, 1, 8, 7, 3, 4]
sorted_test = selectSort(test)  # the algorithm is designed to create/return a new list

print('Sorted:', sorted_test)

