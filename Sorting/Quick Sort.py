Quick Sort : Quicksort is a sorting algorithm based on the divide and conquer approach where an array is divided into subarrays by selecting a pivot element (element selected from the array).
    
While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot. 
The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element. At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        smaller = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)


arr = [8, 7, 2, 1, 0, 9, 6]
print(quick_sort(arr))
