#!/bin/python3

# https://www.hackerrank.com/challenges/extra-long-factorials

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extra_long_factorials(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= int(i)
    print(factorial)


if __name__ == '__main__':
    n = int(input().strip())

    extra_long_factorials(n)
