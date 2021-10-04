def solution(N):
    x = format(N, 'b').strip('0')
    print(x)
    y = x.split('1')
    print(y)
    z = max(y)
    print(z)
    print(len(z))
    return len(max(format(N, 'b').strip('0').split('1')))

result = solution(9)
assert result == 2

result = solution(529)
assert result == 4

result = solution(20)
assert result == 1

result = solution(15)
assert result == 0