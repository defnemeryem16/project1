def max_subarray_brute_force(A):
    n = len(A)
    max_sum = float('-inf')
    start_idx = 0
    end_idx = 0
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += A[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_idx = i
                end_idx = j
                
    return max_sum, start_idx, end_idx