def max_crossing_sum(A, low, mid, high):
    left_sum = float('-inf')
    sum_val = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sum_val += A[i]
        if sum_val > left_sum:
            left_sum = sum_val
            max_left = i
            
    right_sum = float('-inf')
    sum_val = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum_val += A[j]
        if sum_val > right_sum:
            right_sum = sum_val
            max_right = j
            
    return left_sum + right_sum, max_left, max_right

def max_subarray_dac_util(A, low, high):
    if low == high:
        return A[low], low, high
    
    mid = (low + high) // 2
    
    left_sum, l_start, l_end = max_subarray_dac_util(A, low, mid)
    right_sum, r_start, r_end = max_subarray_dac_util(A, mid + 1, high)
    cross_sum, c_start, c_end = max_crossing_sum(A, low, mid, high)
    
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, l_start, l_end
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, r_start, r_end
    else:
        return cross_sum, c_start, c_end

def max_subarray_dac(A):
    if not A:
        return 0, 0, 0
    return max_subarray_dac_util(A, 0, len(A) - 1)