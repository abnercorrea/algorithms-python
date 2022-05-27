"""
Input:

A method getRandom01Biased() that generates a random integer in [0, 1], where 0 is generated with probability p and 1 is generated
with probability (1-p)


Output:

A method getRandom06Uniform() that generates a random integer in [0, 6] with uniform probability
"""
import random
from math import log2, ceil


def getRandom01Biased():
    # not guaranteed implementation but just an example
    return 1 if random.random() >= 0.7 else 0


def getRandom01Uniform():
    """
    Uses von Neumann algorithm
    1. Repeatedly sample two biased samples a, b, until a != b
    2. Return a
    The outcomes (a, b) = (0, 1) and (a, b) = (1, 0) have the same probability, so the bit a (or b) is unbiased.
    """
    a = b = 0

    while a == b:
        a = getRandom01Biased()
        b = getRandom01Biased()

    return a


def getRandomUniform(n: int) -> int:
    num = 0
    for i in range(ceil(log2(n))):
        num += getRandom01Uniform() << i
    if num > n:
        return getRandomUniform(n)
    return num


def getRandom06Uniform():
    return getRandomUniform(6)


def test_get_random_uniform():
    n = 25
    f = 1 / (n + 1)
    tol = f * 0.05
    size = 100000
    distribution = [getRandomUniform(n) for _ in range(size)]
    error = [
        abs((len([x for x in distribution if x == i]) / size) - f)
        for i in range(n + 1)
    ]
    assert all([e <= tol for e in error])
