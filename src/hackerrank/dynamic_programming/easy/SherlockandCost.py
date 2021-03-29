#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    min = 1
    cost_min, cost_max = 0, 0

    for i in range(1, len(B)):
        # max = Bi
        # previous_current naming order
        min_min_delta = 0  # min - min
        max_min_delta = abs(min - B[i - 1])
        min_max_delta = abs(B[i] - min)
        max_max_delta = abs (B[i] - B[i - 1])

        cost_min, cost_max = (
            max(cost_min + min_min_delta, cost_max + max_min_delta),
            max(cost_min + min_max_delta, cost_max + max_max_delta)
        )

    return max(cost_min, cost_max)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
