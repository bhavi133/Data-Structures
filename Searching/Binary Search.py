Binary Search : Binary Search is a searching algorithm for finding an element's position in a sorted array. In this approach, the element is always searched in the middle of a portion of an array.
Note : Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.
  
Binary Search Implementation : Binary Search Algorithm can be implemented in two ways.

1. Iterative Method

def binary_search(arr, key):
    left = 0
    right = len(arr) - 1 
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return f"Element {key} is present at index {mid}"
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return f"Element {key} is not present in array"

arr = [3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 8))
print(binary_search(arr, 2))

2. Recursive Method

def binary_search(arr, left, right, key):
    mid = (left + right) // 2
    if left <= right:
        if arr[mid] == key:
            return f"Element {key} is present at index {mid}"
        elif arr[mid] < key:
            return binary_search(arr, mid+1, right, key)
        else:
            return binary_search(arr, left, mid-1, key)
    else:
        return f"Element {key} is not present in array"

arr = [3, 4, 5, 6, 7, 8, 9]
left = 0
right = len(arr) - 1
print(binary_search(arr, left, right, 8))
print(binary_search(arr, left, right, 2))
