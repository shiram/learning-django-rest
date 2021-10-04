# Given an integer n, return true if it is a power of ten. Otherwise, return false.
# An integer n is a power of ten, if there exists an integer x such that n == 10^x
# print(is_power_of_ten(1))  # true
# print(is_power_of_ten(10))  # true
# print(is_power_of_ten(1000))  # true
# print(is_power_of_ten(5))  # false
# print(is_power_of_ten(20))  # false
# print(is_power_of_ten(-1))  # false
# print(is_power_of_ten(0.00001))  # true

def is_power_of_ten(n):
    if 0 < n < 1:
        while n < 1:
            n *= 10
    elif n >= 10:
        while n > 1:
            n /= 10
    return n == 1

print(is_power_of_ten(1))  # true
print(is_power_of_ten(10))  # true
print(is_power_of_ten(1000))  # true
print(is_power_of_ten(5))  # false
print(is_power_of_ten(20))  # false
print(is_power_of_ten(-1))  # false
print(is_power_of_ten(0.00001))  # true