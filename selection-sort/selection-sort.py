# a Helper function to find the smallest element in the array 
def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr) - 1):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx # returns the index of the smallest number in the array

# selection sort function implementation
def selection_sort(arr):
    newArr = []
    cpdArr = list(arr) # make  a copy of the array before mutation (we work with the copy)
    for i in range(len(cpdArr)):
        smallest = find_smallest(cpdArr)
        newArr.append(cpdArr.pop(smallest))
    return newArr


print(find_smallest([5, 3, 6, 2, 10]))
print('\n###############################\n')
print(selection_sort([5, 3, 6, 2, 10]))