# Write a function that returns the Fibonacci sequence up to a given number of elements.

def fibonacci(n: int) -> list:
    sequence = [0, 1];
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2];
        sequence.append(next_number);
    return sequence;

