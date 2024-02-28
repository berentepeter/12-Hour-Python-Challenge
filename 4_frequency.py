# Frequency Counter: Develop a function that takes a list of numbers 
# and returns a dictionary with keys being the numbers and values 
# being the frequency of those numbers in the list.

def frequency_counter(numbers: list) -> dict:
    frequency = {};
    for x in numbers:
        if x not in frequency.keys():
            frequency[x] = 1;
        else:
            frequency[x] += 1; 
    return frequency;

