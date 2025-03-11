from time import perf_counter


# Big O Notation 
# O(1) - Constant Time Complexity
def get_first_item(array):
    return (array[0])
#  O(1) - Constant Time Complexity
#  Because we are only returning the first element in the array,
#  regardless of the size of the array.


# O(log n) - Logarithmic Time:
# Example: Binary search in a sorted array.
def binary_search(array,target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# O(log n) - Logarithmic Time Complexity
# Because the number of operations is reduced by half in each iteration.
# This is why it's called Logarithmic Time Complexity.
binary_search([1,2,3,4,5,6,7,8,9,10], 5)
# Output: 4

#  This means the target number 5 is at index 4 in the array.
#  The time complexity of this function is O(log n) because the number of operations is reduced
#  by half in each iteration.
#  This is why it's called Logarithmic Time Complexity.
# first iteration: 10/2 = 5
# second iteration: 5/2 = 2.5
# third iteration: 2.5/2 = 1.25
# fourth iteration: 1.25/2 = 0.625
# The number of operations is reduced by half in each iteration.
# This is why it's called Logarithmic Time Complexity.


nemo = ['nemo']

def find_nemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found Nemo!')
            
find_nemo(nemo);
# Output: Found Nemo!

#Analysis:
# O(n) --> Linear Time Complexity
# Because of the for loop, the time complexity is O(n) --> Linear Time Complexity
# This is because we are checking each element in the array once. 
# The number of operations is directly proportional to the size of the input, which is the number of elements in the array.
# This is why it's called Linear Time Complexity.

fish = ['dory', 'bruce', 'marlin', 'nemo'];
nemo = ['nemo'];
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];
large = ['nemo'] * 10;

def find_nemo2(array):
    t0 = perf_counter()
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found Nemo!')   
    t1 = perf_counter()
    print(f'Time taken: {t1 - t0} seconds') 

find_nemo2(fish);

# Output:
# Found Nemo!
# Time taken: 0.000001 seconds

#Analysis:
# O(n) --> Linear Time Complexity
# Because we are still checking each element in the array once. 
# The number of operations is directly proportional to the size of the input, which is the number of elements in the array. This is why it's called Linear Time Complexity.


# type 3 

def printFirstItemthenFirstHalfthenSayHi10Times(items):
    print(items[0]) 
    # O(1) - Constant Time Complexity
    
    middleIndex = len(items) // 2
    index = 0
    
    
    while index < middleIndex:
        print(items[index])
        index += 1 
    # O(n/2) - Linear Time Complexity with respect to n elements
        
    for i in range(10):
        print('Hi!') # O(10)
    # O(10) - Constant Time Complexity
    # O(n/2) + O(10) = O(n) --> Linear Time Complexity
        

# O (n^2) - Quadratic Time Complexity

boxes = ['a', 'b', 'c', 'd', 'e']
def printBoxes(boxes):
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            print(boxes[i], boxes[j])

printBoxes(boxes)

# Analysis:
# O(n^2) - Quadratic Time Complexity
# Because we are checking each element in the array once, and then checking each element in th
# array again for every element in the array.
# The number of operations is directly proportional to the square of the size of the input, which is the number of elements in the array.
# This is why it's called Quadratic Time Complexity.


def printAllnumberthenAllPairSums(numbers):
    print("Number", numbers)
    
    for number in numbers:
        print(number)
    # O(n) - Linear Time Complexity
    
    for firstNumber in numbers:
        for secondNumber in numbers:
            print(firstNumber + secondNumber)
            # O(n^2) - Quadratic Time Complexity
    
    
printAllnumberthenAllPairSums([1, 2, 3, 4, 5]);
 # O(n) + O(n^2) = O(n^2) --> Quadratic Time Complexity
 

# O(2^n) - Exponential Time
def fibonacci(n):
    if n <=1:
        return n
    return fibanacci(n-1) + fibanacci(n-2)
# O(2^n) - Exponential Time Complexity
# Because the number of operations is directly proportional to the size of the input, 
# which is the number of elements in the array.
# This is why it's called Exponential Time Complexity.

# O(n log n) - Linearithmic Time:
Example: Mergesort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # O(n log n)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
# O(n log n) - Linearithmic Time Complexity
# Because the number of operations is directly proportional to the size of the input,
# which is the number of elements in the array.
# This is why it's called Linearithmic Time Complexity.

merge_sort([1, 3, 2, 4, 5, 7, 6, 8, 9, 10])
# how ? 
# 1. divide the array into two halves
# 2. sort the left half
# 3. sort the right half
# 4. merge the two halves together
# 5. return the sorted array
# O(n log n) - Linearithmic Time Complexity