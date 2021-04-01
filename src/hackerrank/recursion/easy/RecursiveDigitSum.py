#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    def super_digit_r(m):
        if len(m) == 1:
            return m
        
        digit_sum = sum([int(digit) for digit in str(m)])
        return super_digit_r(str(digit_sum))
    
    return super_digit_r(super_digit_r(n) * k)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
