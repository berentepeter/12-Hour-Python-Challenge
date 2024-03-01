# Write a function that checks if a given string is a valid email address 
# (contains one '@' and at least one '.').

import re

def email_validator(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';
    if re.match(pattern, email):
        return True;
    else:
        return False;
