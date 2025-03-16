# Quick Sort is another divide-and-conquer algorithm. 
# It picks an element as a pivot and partitions the array around the pivot, 
# recursively sorting the sub-arrays.

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [63, 33, 23, 10, 24, 19, 92, 29]
    print("Quick Sort Result:", quick_sort(arr))
    
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n²)