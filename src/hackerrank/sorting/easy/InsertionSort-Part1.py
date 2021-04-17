#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    e = arr[-1]
    i = 0
    while arr[i] < e:
        i += 1
    for j in range(len(arr) - 1, i, -1):
        arr[j] = arr[j - 1]
        print(str(arr).replace(',', '').replace('[', '').replace(']', ''))
    arr[i] = e
    print(str(arr).replace(',', '').replace('[', '').replace(']', ''))

    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
