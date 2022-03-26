#!/bin/python3


def power_sum_rec(X, powers, sum, i):
    if i == len(powers):
        return 0

    combinations = 0

    for j in range(i, len(powers)):
        new_sum = sum + powers[j]
        if new_sum == X:
            combinations += 1
        elif new_sum < X:
            combinations += power_sum_rec(X, powers, new_sum, j + 1)

    return combinations


def power_sum(X, N):
    max_n = int(X ** (1 / N))
    powers = [i ** N for i in range(1, max_n + 1)]
    return power_sum_rec(X, powers, sum=0, i=0)


if __name__ == '__main__':
    print(power_sum(10, 2))
    print(power_sum(100, 2))
    print(power_sum(100, 3))
    print(power_sum(160000, 4))
