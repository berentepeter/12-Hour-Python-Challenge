# Create a function that counts how many times 
# a word occurs in a sentence (passed as a string).

def word_occurence(sentence: str, word: str) -> int:
    return sentence.lower().split().count(word.lower());

