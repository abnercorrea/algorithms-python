#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    if len(arr) == 0:
        return []
    pivot = arr[0]
    equal = [a for a in arr if a == pivot]
    left = quickSort([a for a in arr if a < pivot])
    right = quickSort([a for a in arr if a > pivot])
    return left + equal + right
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
