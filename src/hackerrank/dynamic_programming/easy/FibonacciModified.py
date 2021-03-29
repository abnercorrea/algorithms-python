#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    if n == 2:
        return t2
    n_minus_1 = t2
    n_minus_2 = t1
    f = 0
    for i in range(n - 2):
        f = n_minus_1 ** 2 + n_minus_2
        n_minus_1, n_minus_2 = f, n_minus_1
    return f

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
