# write a code that gennerates a random binary string of length n
# and counts the number of 1s in the string

import random

def random_binary_string(n):
    binary_string = ""
    for i in range(n):
        binary_string += str(random.randint(0,1))
    return binary_string



if __name__ == '__main__':
    string_lengths = [10, 25, 50]

    for n in string_lengths:
        print(random_binary_string(n))




