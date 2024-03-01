# List Flattener: Develop a function that takes a list of lists 
# and flattens it to a single list without using any built-in Python flattening functions.

def flatten_list(nested_list: list) -> list:
    flat_list = [];
    for i in nested_list:
        flat_list += i;
    return flat_list;

lst = [[1,2,3,], [4,5,6], [4,8,15,16,23,42]];
print(flatten_list(lst))