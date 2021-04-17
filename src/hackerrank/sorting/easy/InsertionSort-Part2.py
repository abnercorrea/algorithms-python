#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    e = arr[n - 1]
    i = 0
    while arr[i] < e:
        i += 1
    for j in range(n - 1, i, -1):
        arr[j] = arr[j - 1]
    arr[i] = e

    # Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        insertionSort1(i + 1, arr)
        print(str(arr).replace(',', '').replace('[', '').replace(']', ''))
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
