# Binary Search Python Code
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        guess = (low + high) // 2
        if arr[guess] == item:
            return guess
        elif arr[guess] > item:
            high = guess - 1
        else:
            low = guess + 1
    return None



print(binary_search([1, 3, 5, 7, 9], 7))
print(binary_search([1, 3, 5, 7, 9], 8))
print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9], 9))

