def max_subarray_kadane(A):
    if not A:
        return 0, 0, 0
        
    max_so_far = A[0]
    curr_max = A[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(A)):
        if A[i] > curr_max + A[i]:
            curr_max = A[i]
            temp_start = i
        else:
            curr_max += A[i]
            
        if curr_max > max_so_far:
            max_so_far = curr_max
            start = temp_start
            end = i
            
    return max_so_far, start, end