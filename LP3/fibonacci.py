# Program to generate Fibonacci sequence
# using Recursive and Non-Recursive Functions


# Recursive function to find nth Fibonacci number
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Non-Recursive (Iterative) function to generate sequence
def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


# Main Program
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("\nFibonacci Sequence:")
    print(fibonacci_iterative(n))

    print("\nComplexity Analysis:")
    print("1. Recursive Method")
    print("   Time Complexity : O(2^n)")
    print("   Space Complexity: O(n)")

    print("\n2. Non-Recursive (Iterative) Method")
    print("   Time Complexity : O(n)")
    print("   Space Complexity: O(1)")
