# Prime Number Finder: Write a function that takes an integer 
# and returns a list of all prime numbers up to and including that integer.
import math

def find_primes(n: int) -> list:
    primes = [];
    isPrime: bool;
    for i in range(2, n + 1):
        isPrime = True;
        for j in range(2, math.isqrt(i) + 1):
            if (i % j == 0):
                isPrime = False;
        if(isPrime == True):
            primes.append(i);        
    return primes;

