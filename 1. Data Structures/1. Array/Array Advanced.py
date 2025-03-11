# Advanced Array
numbers = [1, 2, 3, 4, 5]

#Rotating a list to the right
def rotate_right(list, k):
    k = k % (len(list))
    return list[-k:] + list[:-k]

rotated = rotate_right(numbers, 2)
print(rotated)

# Checking if a list is a palindrome
is_palindrome = lambda list: list == list[::-1]
print(is_palindrome([1, 2, 3, 2, 1]))
# # Checking if a list is a palindrome
# def is_palindrome(list):
#     return list == list[::-1]

# lambda list: list == list[::-1]
# explanation:
# list[::-1] returns a reversed list
# list == list[::-1] returns True if the list is a palindrome

# Using zip() to combine two lists
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 28]
combined_list = list(zip(names,ages))
print(list(combined_list))

# Counting occurrences of elements
list1 = [1, 2, 3, 4, 1, 2, 1, 2, 1]
from collections import Counter
freq = Counter([1, 2, 3, 4, 1, 2, 1, 2, 1])
freq2 = Counter(list1)
print(freq)
print(freq2)

text = "Hello world this is a test  text file Hello World"
words = text.lower().split()
freq_text = Counter(words)
print(freq_text)

# Creating a list of random numbers
import random
random_num = [random.randint(1,100) for _ in range(100)]
#print(random_num)

# Finding the index of the first occurrence of a value in a list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index_of_5 = list1.index(5) if 5 in list1 else -1
print(index_of_5)

# Creating a list of strings with their lengths
words = ["apple", "banana", "cherry"]
length_of_words = [len(word) for word in words]
print(length_of_words)
length2 = {}
for word, length in zip(words, length_of_words):
    if length not in length2:
        length2[length] = [word]
    else:
        length2[length].append(word)
print(length2)

# same as using Counter
length3 = Counter(len(word) for word in words)
print(length3)

# Creating a list of tuples (number, square)
number_square = [(x, x**2) for x in range(1,6)]
print(number_square)

# Using lambda to sort a list of tuples by the second element
tuples_list = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
sorted_tuples_list = sorted(tuples_list, key=lambda x:x[1])
print(sorted_tuples_list)

# Merging two lists while preserving order and uniqueness
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

def merge_unique(list1, list2):
    merged = []
    seen = set()
    
    for item in list1 + list2:
        if item not in seen:
            merged.append(item)
            seen.add(item)
    return merged

merged_list = merge_unique(list1, list2)
print(merged_list)

# Creating a list of factorials using a loop

factorials = []

for i in range(6):
    if i == 0:
        factorials.append(1)
    else:
        factorials.append(factorials[-1]*i)
print(factorials)

#method 2:
import math
factorials2 = {i:math.factorial(i) for i in range(6)} 
for number, fact in factorials2.items():
    print(f"{number}! = {fact}") 

# Using list comprehension to create a list of tuples (number, is_even)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
is_even = [(x, x%2==0) for x in numbers]
print(is_even)

#  create a list of squares
squares_gen =  (x**2 for x in numbers)
print(list(squares_gen))

# Creating a list of unique characters from a string
text = "hello world"
unique_chars = list(set(text))
print(unique_chars)

# to maintain the order:
unique_char = []

for char in text:
    if char not in unique_char:
        unique_char.append(char)
print(unique_char)

# Using a list to implement a stack
stack = []
stack.append(1) # push
stack.append(2)
stack.append(3)
top_element = stack.pop()
print(top_element) 

# Using a list to implement a queue
queue = []
queue.append(1) # enqueue
queue.append(2)
queue.append(3)
first_element = queue.pop(0)
print(first_element)

## Important note: queue is not good with List due to bad space complexity as it has to 
# adjust the index of all elements when pop(0) is called
# LinkedList is preferred for queue

# List slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_numbers = numbers[2:7]
print(sliced_numbers)

# Using enumerate to get index and value
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")
    
# Using all() to check if all elements are positive
all_positive = all(x > 0 for x in numbers)
print(all_positive)

# Using any() to check if any element is even
any_even = any(x%2==0 for x in numbers)
print(any_even)

# Using reduce() to calculate the product of elements
from functools import reduce
product = reduce(lambda x,y: x * y, numbers)
print(product)

# Using sorted() with a custom key
words = ["apple", "banana", "cherry", "date"]
sorted_key = sorted(words, key=len)
print(sorted_key)

# Using set() to find unique elements
list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
unique_numbers = set(list1)
print(unique_numbers)

# Nested list comprehensions for matrix transposition
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

# Using itertools for combinations
from itertools import combinations
comb = combinations(numbers,2)
print(list(comb))

# Using deque for efficient queue operations
from collections import deque
# deque is preferred over list for queue operations
queue = deque()
queue.append(1) # enqueue
queue.append(2)
queue.append(3)
first_element = queue.popleft() # dequeue
print(first_element)