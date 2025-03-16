# Heap Sort is a comparison-based sorting algorithm that uses a 
# binary heap data structure. It first builds a max heap from the 
# input data, then repeatedly extracts the maximum element from the 
# heap and rebuilds the heap until the array is sorted.

def _heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right 
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n //2 -1, -1, -1):
        _heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    
    return arr
       
if __name__ == "__main__":
    arr = [63, 33, 23, 10, 24, 19, 92, 29]
    print("Heap Sort Result:", heap_sort(arr))       
        