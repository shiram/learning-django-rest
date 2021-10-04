"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""

def solution_score_100(A):
    # write your code in Python 3.6

    # This solution will run in time complexity O(n) space complexity of O(n)
    A_len = len(A)
    A_sorted = sorted(A)

    if A_sorted[0] != 1:
        return 0
    elif A_len == 1 and A_sorted[0] != 1:
        return 0
    elif A_len > 1:
        checker = 1
        for element in A_sorted:
            if checker == element:
                checker += 1
            else:
                return 0
    return 1

def solution_score75(A):
    # write your code in Python 3.6
    A_len = len(A)
    sumN = sum(i for i in range(1, A_len + 1))
    if sumN == sum(A):
        return 1
    return 0