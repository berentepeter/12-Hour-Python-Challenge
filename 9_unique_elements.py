# Write a function that returns the unique elements in a list.

def unique_elements(lst: list) -> list:
    uniques = [];
    for x in lst:
        if x not in uniques:
            uniques.append(x);
        else:
            continue 
    return uniques;

