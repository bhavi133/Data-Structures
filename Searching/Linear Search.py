Linear Search : Linear Search is one of the searching algorithm . It is also called as sequential algorithm. It compares each and every element with the value that we are searching for.
If both are matched, the element is found, and the algorithm returns the key's index position.

def linear_search(arr, key):
    flag = 0
    for i in range(len(arr)):
        if arr[i] == key:
            flag = 1
            break
        else:
            flag = 0
    
    if flag == 1:
        return f"Element {key} is present at index {i+1}"
    else:
        return f"Element {key} is not present in array"


arr = [4, 2, 3, 10, 7, 9]
print(linear_search(arr, 8))
print(linear_search(arr, 3))
