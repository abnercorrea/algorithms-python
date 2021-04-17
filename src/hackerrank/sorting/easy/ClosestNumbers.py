#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    s = sorted(arr)
    diff = [s[i] - s[i - 1] for i in range(1, len(s))]
    min_diff = min(diff)
    min_diff_ind = [i for i, d in enumerate(diff) if d == min_diff]
    closest_numbers = []
    for i in min_diff_ind:
        closest_numbers += [s[i], s[i + 1]]
    return closest_numbers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
