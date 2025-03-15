# Dynamic programming is a powerful technique for solving optimization 
# problems by breaking them down into simpler subproblems 
# and storing the results to avoid redundant calculations.

# Recursive Fibonacci (Inefficient)

def fibonacci_recursive(n):
    if n <= 0:
        return 0 
    elif n ==1:
        return 1 
    else:
        return fibonacci_recursive(n -1) + fibonacci_recursive(n -2)

if __name__ == "__main__":
    num = 6
    print(f"The {num}th fibonacci number(recursive) {fibonacci_recursive(num)}")
    
# Time Complexity: O(2^n) due to the exponential growth of recursive calls.
# Space Complexity: O(n) due to the recursion stack

#Dynamic Programming Fibonacci (Efficient)

def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    else:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        return memo[n]
if __name__ == "__main__":
    num = 10
    print(f"The {num}th Fibonacci Number(memoization): {fibonacci_memoization(10)}")
    
# Time Complexity: O(n) because each Fibonacci number is computed only once.
# Space Complexity: O(n) for the memoization dictionary.
    
# Example 2: Coin Change Problem

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    coins = [3,6,9]
    amount = 33
    print(f"Minimum coins needed to make {amount}: {coin_change(coins, amount)}")  