# write a sum function that sums a list elements (recursivly)

def sum(L):
    if len(L) == 1:
        return L[0]
    return L[0] + sum(L[1:])

# print(sum([2, 4, 6]))

# write a recursive function that count the List items
def count_items(L):
    if len(L) == 1:
        return len([L[0]])
    return len([L[0]]) + count_items(L[1:])

# print(count_items([2, 4, 6]))

# //////////////////////////////////////

# write a recursive function that finds the maximum number in alist

def max_recur(L):
    sorted_L = sorted(L)
    if len(sorted_L) == 1:
        return sorted_L[0]
    return max_recur(sorted_L[1:])
# print(max_recur([2, 4, 6]))
# print(max_recur([5, 3, 10, 35, 20]))


# recursive binary search approach
def binary_search_recur(L, i, low = 0, heigh = None):
    if heigh is None:
        heigh = len(L) - 1
    mid = (low + heigh) // 2
    if low >= heigh:
        return -1
    if L[mid] < i:
       return binary_search_recur(L, i, mid + 1)
    elif L[mid] > i:
        return binary_search_recur(L, i, mid, mid - 1)
    return mid
print(binary_search_recur([1, 3, 5, 7, 9], 7))