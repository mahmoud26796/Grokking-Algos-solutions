# quick sort code 
# we can use list comprehension in python 
# but i wanted to make it very obvious
def quick_sort(L):
    if len(L) < 2:
        return L
    start = 0
    end = len(L) - 1
    mid = (start + end) // 2
    pivot = L[mid]
    left_L = []
    right_L = []
    piv_L = [pivot]
    for i in range(start, mid):
        if L[i] > pivot:
            right_L.append(L[i])
        else:
            left_L.append(L[i])
    for i in range(mid + 1, end + 1):
        if L[i] > pivot:
            right_L.append(L[i])
        else:
            left_L.append(L[i])

    return quick_sort(left_L) + piv_L + quick_sort(right_L)


print(quick_sort([2, 1, 3, 5, 4]))