"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_score_100(A):
    # Time Complexity: O(n) or O(n*log(n))
    # Space Complexity: O(n)
    N = len(A)
    if N < 1:
        return 1
    elif N == 1 and A[0] != 1:
        return 1
    elif N == 1 and A[0] == 1:
        return A[0] + 1
    elif N > 1:
        sorted_A = sorted(A)
        smallest_int = 1
        if sorted_A[0] > 1:
            return smallest_int
        for i in range(N - 1):
            if sorted_A[i] > 0 and sorted_A[i + 1] > 0:
                if sorted_A[i + 1] - sorted_A[i] > 1:
                    return sorted_A[i] + 1 if sorted_A[i] > 0 else sorted_A[i + 1] - 1
                smallest_int =  sorted_A[i + 1] +1
        return smallest_int
