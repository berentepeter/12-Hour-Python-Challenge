# Palindrome Checker: Create a function that checks if a given string is 
# a palindrome (reads the same backward as forward, ignoring spaces, 
# punctuation, and capitalization).

def is_palindrom(s: str) -> bool:
    clean_str = s.replace(' ', '').lower();
    reversed_str = reversed(clean_str);
    if list(reversed_str) == list(clean_str):
        return True;
    else:
        return False;
