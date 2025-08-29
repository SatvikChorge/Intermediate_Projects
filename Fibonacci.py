def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input: number of terms
terms = int(input("Enter the number of terms in the Fibonacci series: "))
if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Series:")
    print(fibonacci_series(terms))