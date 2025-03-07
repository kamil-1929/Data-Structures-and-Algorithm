from time import perf_counter


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
 
