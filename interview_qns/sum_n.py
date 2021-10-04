import timeit

def sum_n_m(N):
    start_time = timeit.default_timer()
    return (N * (N + 1) // 2 , start_time - timeit.default_timer())

def sum_n_f(N):
    start_time = timeit.default_timer()
    result = 0
    for i in range(N):
        result += i + 1
    return result, start_time - timeit.default_timer()

def sum_n_s(N):
    start_time = timeit.default_timer()
    result = 0
    for i in range(N):
        for j in range(i + 1):
            result += 1
    return result , start_time - timeit.default_timer()

res = sum_n_m(5)
print("The answer and runtime for sum_n_m: {} ".format(res))

res = sum_n_f(5)
print("The answer and runtime for sum_n_f: {} ".format(res))

res = sum_n_s(5)
print("The answer and runtime for sum_n_s: {}".format(res))