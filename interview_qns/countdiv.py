"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B
"""

def solution_score_50(A, B, K):
    # write your code in Python 3.6
    divisible_count = 0
    for i in range(A, B + 1):
        if i % K == 0:
            divisible_count += 1
    return divisible_count

def solution_score_25(A, B, K):
    # write your code in Python 3.6
    divisible_count = 0
    while A <= B:
        if A % K == 0:
            divisible_count += 1
        A += K
    return divisible_count

def solution_score_100(A, B, K):
    # write your code in Python 3.6
    """
    To get multiples of K from A - B.
    Get multiples of K in range B = B // K say kB
    get multiples of K before A: A - 1 // K asy kA
    return difference kB - kA. this gives the multiples of K from A to B
    """
    return (B // K) - ((A - 1) // K)