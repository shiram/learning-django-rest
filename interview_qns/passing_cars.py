"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""

from itertools import count

def solution_score_50(A):
    #Time complexity: O(n**2)
    N = len(A) #Lenght of Array A.
    pair_cars = []
    for car_east in range(N):
        if A[car_east] == 0: #found car moving east
            for car_west in range(car_east + 1, N): #find cars moving in west.
                if A[car_west] == 1:
                    pair_cars.append((car_east, car_west)) # if car moving west, add pair to list.
    if len(pair_cars) > 1000000000: #check if pairs exceed 1 billion.
        return -1
    return len(pair_cars)

def solution_score50b(A):
    #Time complexity: O(n**2)
    # write your code in Python 3.6
    N = len(A) #Lenght of Array A.
    if not (1 <= N <= 100000):
        return False
    pair_cars = []
    for car_east in range(N):
        if A[car_east] == 0: #found car moving east
            for car_west in range(car_east + 1, N): #find cars moving in west.
                if A[car_west] == 1:
                    if 0 <= car_east < car_west < N:
                        pair_cars.append((car_east, car_west)) # if car moving west, add pair to list.
    if len(pair_cars) > 1000000000: #check if pairs exceed 1 billion.
        return -1
    return len(pair_cars)

def solution_score_50c(A):
    road_dict = {key: value for key, value in enumerate(A)}
    print(road_dict)
    pairs = 0
    for item in road_dict:
        if road_dict[item] == 0:
            pairs += sum([i for i in road_dict if road_dict[i] == 1 and i > item])
    if pairs > 1000000000:
        return -1
    return pairs

def solution_score_60(A):
    west_tr = [i for i, j in zip(count(), A) if j == 1]

    east_tr = [i for i, j in zip(count(), A) if j == 0]
    pairs = 0
    for i in east_tr:
        if i == 0:
            pairs += len(west_tr)
        else:
            pairs += len([c for c in west_tr if c > i])
    if pairs > 1000000000:
        return -1
    return pairs

def solution_score_100(A):
    # Time Comolexity: O(n)
    # Space Complexity: O(1)
    pairs, car_east= 0, 0
    for car in A:
        if car == 0:
            car_east += 1
        if car_east > 0:
            if car == 1:
                pairs = pairs + car_east
                if pairs > 1000000000:
                    return -1
    return pairs





A = [0, 1, 0, 1, 1]

res = solution_score_100(A)

assert res == 5