# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result += left[i:]

    elif j < len(right):
        result += right[j:]

    return result

a = [6,4,1,3,7,2,8,5]

print(merge_sort(a))

# - Normally, a merge sort runs at O(NlogN) time complexity. The depth of the recursive tree of merge sort function is logN, and each level runs at O(N).
# - However, in our merge sort code, the while loop runs O(M+N) times, where M and N are the length of the two input list, and the list slicing method runs O(M) or O(N) times.
# - So the total time complexity of our merge function is O(M^2 + N^2).
# - This makes the time complexity of our merge sort program O(N^2 * logN) instead of O(NlogN)
#
# - To optimize the code, we can rewrite the merge function to use pointers to keep track of the smallest value in each list when merging so that the merge function can run at O(M+N) time complexity.
# Optimized version: https://replit.com/join/gcankruryq-andrewwen2