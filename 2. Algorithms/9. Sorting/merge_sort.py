# Merge Sort is a divide-and-conquer algorithm that divides the input 
# array into two halves, sorts them, and then merges the sorted halves.

def _merge(arr1, arr2):
    combined = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:
            combined.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        combined.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        combined.append(arr2[j])
        j += 1
        
    return combined
     
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid_index = int(len(arr) // 2)
    left = merge_sort(arr[:mid_index])
    right = merge_sort(arr[mid_index:])
    
    return _merge(right, left)

if __name__ == "__main__":
    arr = [63, 33, 23, 10, 24, 19, 92, 29]
    print("Merge Sort Result:", merge_sort(arr))
    
# Time Complexity
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n)