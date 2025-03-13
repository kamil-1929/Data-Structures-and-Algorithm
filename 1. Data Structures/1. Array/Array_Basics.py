# Create a new List
numbers = [1,2,3,4,5,6,7,8,9,10]

#Accessing the elements of an array
first_element = numbers[0]
last_element = numbers[-1]

# Modifying the elements of an array
numbers[0] = 10 # Change 1 to 10
numbers[-1] = 1 # Change 10 to 1
print(numbers[0]) # Output: 10

#Appending a new element
numbers.append(11)
print(numbers)

# Inserting a new element at a specific index
numbers.insert(3, 5)    
print(numbers)

# Removing an element
numbers.remove(4)
print(numbers)

# Removes the last element
numbers.pop() 
print(numbers)

#Checking for the presence of an element
if 5 in numbers:
    print("Yes")
    
print(5 in numbers)

# Finding the index of an element
index_of_5 = numbers.index(5)
print(index_of_5)
print(numbers.index(5))

# sorting the list
numbers.sort() # Ascending order
print(numbers)

#Reversing the list
numbers.reverse()   
print(numbers)

#List Comprehension for squaring the elements of a list
squared_numbers = [i**2 for i in numbers]
square_even_num = [i**2 for i in numbers if i%2==0 ]
square_odd_num = [i **2 for i in numbers if i%2==1]
print(squared_numbers)
print(square_even_num)
print(square_odd_num)

# Using map() with lambda to double numbers
# what is map()?
# map() is a built-in Python function used to apply a function to a sequence of elements like a list or dictionary.
# It returns a map object which can be converted into a list or tuple.
# The map() function takes two arguments: a function and a sequence iterable.
# The function is the one that will be applied to each element of the iterable.

double_numbers = list(map(lambda x:x*2, numbers))
print(double_numbers)

# Using filter() with lambda to filter even numbers
# what is filter()?
# filter() is a built-in Python function used to filter elements from a sequence like a list or dictionary.
# It returns a filter object which can be converted into a list or tuple.
# The filter() function takes two arguments: a function and a sequence iterable.
odd_numbers = list(filter(lambda x:x%2==1, numbers))
print(odd_numbers)

# Using reduce() with lambda to sum numbers
# what is reduce()?
# reduce() is a built-in Python function used to reduce a sequence of elements into a single element.
# It returns a single value.
# The reduce() function takes two arguments: a function and a sequence iterable.
from functools import reduce
sum_numbers = reduce(lambda x, y : x + y, numbers)
sum_numbers_with_initialization = reduce(lambda x, y : x + y, numbers,  10)
print(sum_numbers)
print(sum_numbers_with_initialization)


# Using zip() to combine two lists
# what is zip() ?
# zip() is a built-in Python function used to combine two or more lists into a single list.

list1 = [1,2,3,4,5,6,7]
list2 = ['a','b','c','d','e','f','g']
zipped_list = list(zip(list1, list2))
print(zipped_list)

# Using * to unpack a list
# what is *?
# The * operator can be used to unpack a list or tuple.
# It can also be used to unpack a dictionary.
unpacked_list = list(zip(*zipped_list))
print(unpacked_list)

# Using enumerate() to get both index and value of a list
# what is enumerate()?
# enumerate() is a built-in Python function used to get both the index and value of a list.
# It returns an enumerate object which can be converted into a list or tuple.
# The enumerate() function takes a sequence iterable as an argument.

for index, value in enumerate(list1):
    print(f"Index:{index}, Value:{value}")
   
# Creating a list of tuples 
list_of_tuples1 = [(1, 'a'), (2, 'b'), (3, 'c')]
# Unpacking a list of tuples
for x, y in list_of_tuples1:
    print("list_of_tuples1: ",x,y)   
    
# tuples are ordered and unchangeable and tuples are written with round brackets 
# tuples can have duplicate values and immutable objects
list_of_tuples = [[(1, 'a'), (2, 'b'), (3, 'c')], [(4, 'd'), (5, 'e'), (6, 'f')]]
print(list_of_tuples)

# Unpacking a list of list of tuples
unpack_tuples = [item for sublist in list_of_tuples for item in sublist]
print(unpack_tuples)    
    

# Creating a list of Fibonacci numbers
# Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding ones.
# The first two Fibonacci numbers are 0 and 1.
# The next number is found by adding up the two numbers before it.
# The Fibonacci sequence starts with 0 and 1.
fibonacci = [0,1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(10)]
print(fibonacci)

# BIG O
# Access: O(1)
# Search: O(n)
# Space  Complexity: O(n)

# Finding common elements in two lists

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [4,5,6,7,8,9,10,11,12,13]

common_elements = [x for x in list1 if x in list2]
print(common_elements)
#big o notation for this is O(n^2)

# Creating a list of prime numbers
# Prime numbers are numbers that are greater than 1 and have no divisors other than 1 
# and itself.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(50) if is_prime(x)]
print(primes)

# Big O 
'''
Static Array:
Lookup O(1)
Push O(1)
Insert O(n)
Delete O(n)

Dynamic Array:
Lookup O(1)
append O(1)
Insert O(n)
Delete O(n)
'''



