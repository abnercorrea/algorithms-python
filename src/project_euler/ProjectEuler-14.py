MEMOIZE_CAPACITY = 5000001
memoized = [0] * MEMOIZE_CAPACITY
memoized[1] = 1

def collatz_sequence_length(n):
    if memoized[n] != 0:
        return memoized[n]

    if n % 2 == 0:
        memoized[n] = 1 + collatz_sequence_length(n >> 1)
    else:
        c = 3 * n + 1
        steps = 1
        while (c >= MEMOIZE_CAPACITY):
            c = c >> 1 if c % 2 == 0 else 3 * c + 1
            steps += 1
        memoized[n] = steps + collatz_sequence_length(c)

    return memoized[n]


def longest_collatz_sequence(ns):
    n = sorted([i for i in ns if i > 0])
    max_n = n[-1] + 1
    max_length = 0
    longest_n = 0
    result = {}

    ni = 0

    for i in range(1, max_n):
        length = collatz_sequence_length(i)
        if length >= max_length:
            max_length = length
            longest_n = i
        if i == n[ni]:
            result[i] = longest_n
            ni += 1
    return result


def main_hackerrank():
    t = int(input().strip())
    n = [int(input().strip()) for _ in range(t)]
    # n = list(range(10000))
    lcs = longest_collatz_sequence(n)
    for i in n:
        print(lcs[i] if i > 0 else 0)


if __name__ == '__main__':
    # main_hackerrank()
    print(longest_collatz_sequence(range(990000, 1000001)))
