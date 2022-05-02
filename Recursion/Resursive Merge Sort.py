# Recursive Merge Sort Python Implementation
# Top Down Approach


def mergeSort(array):
    if len(array) <= 1:
        return array
    # end of base case

    left = [] # Division of array : left half
    right = [] # Divsion of array : right half

    for i in range(len(array)):
        if i < (len(array) // 2):
            left.append(array[i])
        else:
            right.append(array[i])
    # end of division

    # recursive mergeSort of left and right
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)
# end of mergeSort()

def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    # end of handling left and right

    while left:
        result.append(left[0])
        left = left[1:]

    while right:
        result.append(right[0])
        right = right[1:]

    return result
# end of merge()

test = [6, 5, 3, 1, 8, 7, 3, 4]

sorted_test = mergeSort(test) # creates a new sorted list
print('Sorted:', sorted_test)