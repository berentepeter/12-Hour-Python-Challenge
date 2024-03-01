# Write a function that merges two dictionaries. 
# If there is a conflict between dictionaries (same key), 
# the value from the second dictionary should be kept.

def dict_merge(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy();
    merged_dict.update(dict2);
    return merged_dict;

