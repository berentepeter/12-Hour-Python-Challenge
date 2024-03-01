# Develop a function that prints out a multiplication table 
# for numbers up to a given number.

def multiplication_table(n: int):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} * {j} = {i * j}");
        print();

