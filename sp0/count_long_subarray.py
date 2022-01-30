def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    current = 1
    length = 1
    size = len(A)

    for i in range(1,size):
        if A[i-1] < A[i]:
            current += 1
        else:
            current =1
        if current == length :
            count +=1
        elif current > length:
            length = current
            count = 1
    return count

B = (1,3,4,2,5,7,5,6,9,8)

print (count_long_subarray(B))
