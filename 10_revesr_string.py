# Create a function that takes a string and returns the string in reversed order without using the [::-1] syntax.

def reverse_string(s: str) -> str:
    reversed_str = '';
    return reversed_str.join(reversed(s));
