def longest_mountain(A):
    """
    Return the length of the longest mountain in an array.
    Mountain properties:
        B.length >= 3
        There exists some0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
    """
    longest = 0
    for i in range(1, len(A)-1):
        j, k = i-1, i+1
        if A[j] < A[i] > A[k]:
            size = 3
            while j > 0:
                if A[j-1] < A[j]:
                    size += 1
                    j -= 1
                else:
                    break
            while k < len(A)-1:
                if A[k+1] < A[k]:
                    size += 1
                    k += 1
                else:
                    break
            if size > longest:
                longest = size

    return longest

print(longest_mountain([2,2,2]))  #0
print(longest_mountain([2,1,3,4,7,3,2,1,0,6,7,5]))  #8