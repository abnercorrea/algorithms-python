#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
    return sorted(arr)[len(arr) // 2]

    
def findMedian_v2(arr):
    if not arr:
        return None

    start = 0
    end = len(arr) - 1
    median = len(arr) // 2

    while True:
        pivot = (start + end) // 2
        i = partition(arr, pivot, start, end)

        if i > median:
            end = i - 1
        elif i < median:
            start = i + 1
        else:
            return arr[median]


def partition(a, i, start, end):
    """
    Partitions array using a[i] as pivot and returns the final index of element a[i]
    """
    if not a or start > end:
        return -1

    lo = start
    # last position will be used by a[i]
    hi = end - 1
    a[i], a[end] = a[end], a[i]  # moves a[i] to the end of the array

    while lo <= hi:
        while a[lo] < a[end]:
            lo += 1
        # note h >= 0 to allow h to become -1 in cases where l = h = 0
        while hi >= start and a[hi] > a[end]:
            hi -= 1
        if lo < hi:
            a[lo], a[hi] = a[hi], a[lo]  # swap
            # only move l and h if lo < hi
            lo += 1
            hi -= 1

    # l holds the final position (in order) of the original a[i]
    a[lo], a[end] = a[end], a[lo]

    return lo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
