# Define the maximum limit for Fibonacci sequence
MAX_VALUE = 10000  

# Initialize first two Fibonacci numbers
fib1, fib2 = 0, 1  

# Print the first two numbers
print(fib1, fib2, end=" ")  

# Loop to generate and print Fibonacci numbers until reaching MAX_VALUE
while True:
    next_fib = fib1 + fib2  # Calculate next term
    
    if next_fib >= MAX_VALUE:  # Stop if the number exceeds the limit
        break
    
    print(next_fib, end=" ")  # Print the next Fibonacci number
    
    # Update values for the next iteration
    fib1, fib2 = fib2, next_fib  