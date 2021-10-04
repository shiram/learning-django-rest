def reverse(A):
    """
    reverse an array: [3,6,7,9] = [9,7,6,3]~
    """
    A_len = len(A)
    for i in range(A_len // 2):
        print("-----------------------")
        print("Renge: %s" % i)
        k = A_len - i - 1
        print("k = %s" % k)
        print("Before Change A[i] = %s, A[k] = %s " % (A[i], A[k]))
        A[i], A[k] = A[k], A[i]
        
        print("After Change A[i] = %s, A[k] = %s " % (A[i], A[k]))
        print("Array at time: %s" % A)
        print("------------------------")
    return A
    

A = [3,6,7,9]
result = reverse(A)
assert result == [9,7,6,3]

result = reverse([1,2,3,4,5,6,7])
assert result == [7,6,5,4,3,2,1]

result = reverse([20, 11, 12, 90, 78, 5])
assert result == [5, 78, 90, 12, 11, 20]

result = reverse([5,4,3,9,0])
assert result == [0,9,3,4,5]

result = reverse(['A', 'N', 'K', 'P'])
assert result == ['P', 'K', 'N', 'A']