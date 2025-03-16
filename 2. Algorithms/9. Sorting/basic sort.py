# 1. Bubble Sort
# Bubble Sort is a simple comparison-based sorting algorithm. 
# It repeatedly steps through the list, compares adjacent elements, 
# and swaps them if they are in the wrong order. 
# The pass through the list is repeated until the list is sorted.

def bubble_sort(arr):
    n = len(arr) - 1
    for i in range(n, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr

if __name__ == "__main__":
    arr = [64, 33, 23, 19, 24, 10, 99]
    print("Bubble Sort Result:", bubble_sort(arr))

#2. Selection Sort
# Selection Sort is another simple comparison-based sorting algorithm.
# It divides the input list into two parts: a sorted part and an unsorted part. 
# It repeatedly selects the smallest (or largest) 
# element from the unsorted part and moves it to the sorted part.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = [72, 27, 23, 10, 29, 92, 91]
    print("Selection Sort Result:", selection_sort(arr))            
    
#3. Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while temp < arr[j] and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -=1
    return arr

if __name__ == "__main__":
    arr = [72, 27, 23, 10, 29, 92, 91]
    print("Insertion Sort Result:", insertion_sort(arr))            
    
# Big O(n^2)
# for almost sorted array then it is O(n)

