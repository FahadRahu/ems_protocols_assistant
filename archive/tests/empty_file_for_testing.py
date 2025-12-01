"""The file test_scraped_functions is a log of random functions and other code I tested or may not
have used. This file should remain empty. It's just an empty space to test out code for it to be
deleted right after."""

import numpy as np

a = np.random.randint(0, 5, (4, 3))
print(f"a is {a.shape} and is: \n{a}\n") # a.shape is 4,3: prints a 4x3 array of random integers between 0 and 9
b = np.random.randint(0, 5, (4, 1)) # b.shape is 4,1: prints a 4x1 array of random integers between 0 and 9
print(f"b is {b.shape} and is: \n{b}\n")
c = np.zeros((a.shape[0], a.shape[1]))

for i in range(a.shape[1]):
    for j in range(a.shape[0]):
        print((f"Before addition, c[{j},{i}] is {c[j,i]}, a[{j},{i}] is {a[j,i]}, "))
        c[j,i] = a[j,i] + b[j][0]  # adds corresponding elements of a and b

print(f"c after addition is {c.shape} and is: \n{c}\n")