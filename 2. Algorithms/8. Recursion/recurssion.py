# # Understanding Recursion

# A recursive function typically has two main components:

# Base Case: This is the condition under which the recursion stops. 
# It prevents the function from calling itself indefinitely.
# Recursive Case: This is where the function calls itself with a modified 
# argument, moving towards the base case.

# Example: factorial 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is : {factorial(num)}")
    
# Time Complexity: O(n) because the function makes ( n ) recursive calls.
# Space Complexity: O(n) due to the recursion stack, 
# which can grow up to ( n ) in the worst case.

#Example: Fibonacci Sequence

def fibonacci(n):
    if n <= 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
if __name__ == "__main__":
    num = 6
    print(f"The {num}th fibonacci number is: {fibonacci(num)}")
    
# Time Complexity: O(2^n) because each call to fibonacci results in 
# two more calls, leading to an exponential growth in the number of calls.
# Space Complexity: O(n) due to the recursion stack.


# Example: Tower of Hanoi
#  The objective is to move a stack of disks from one peg to another, 
# following specific rules.
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 
    tower_of_hanoi(n-1, source, auxiliary, target) # Move n-1 disks to auxiliary
    print(f"Move disk{n} from {source} to {target}") # Move the nth disk to target
    tower_of_hanoi(n-1, auxiliary, target, source) # Move n-1 disks from auxiliary to target
    
if __name__ == "__main__":
    num_disks = 3
    print("Steps to solve Tower of Hanoi:")
    tower_of_hanoi(num_disks, 'A', 'C', 'B')  # A, B, C are the names of the pegs

# Time Complexity: O(2^n) because each disk requires two moves for every 
# additional disk.
# Space Complexity: O(n) due to the recursion stack.