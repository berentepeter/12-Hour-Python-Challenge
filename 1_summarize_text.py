# Function to Summarize a Text File: 
# Write a function that accepts a filename as a parameter, 
# reads the file, and returns the number of lines, words, and characters in the file.


def summarize_text_file(filename):
    
    with open(filename, 'r') as file:
        content = file.read()
        line = 1;
        word = 0;
        char = 0;
        for i in content:
            if i == '\n':
                line += 1;
        words = content.split();
        word += len(words);
        char += len(content);
    return  line, word, char

res = summarize_text_file("test.txt");
print(f"lines: {res[0]} words: {res[1]} characters: {res[2]}");
