import time
import matplotlib.pyplot as plt

# ==========================================
# 1. BRUTE-FORCE ALGORITHM: O(n^2)
# ==========================================
def max_subarray_brute_force(A):
    n = len(A)
    max_sum = float('-inf')
    start_idx, end_idx = 0, 0
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += A[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_idx = i
                end_idx = j
                
    return max_sum, start_idx, end_idx

# ==========================================
# 2. DIVIDE AND CONQUER ALGORITHM: O(n log n)
# ==========================================
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

# ==========================================
# 3. KADANE'S ALGORITHM: O(n)
# ==========================================
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

# ==========================================
# TESTING & BENCHMARKING SCRIPT
# ==========================================
if __name__ == "__main__":
    # Test Arrays specified in project instructions
    A1 = [-2, -5, 6, -2, -3, 1, 5, -6]
    A3 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    
    print("--- VERIFICATION ON TEST ARRAYS ---")
    for name, arr in [("A1", A1), ("A3", A3)]:
        bf = max_subarray_brute_force(arr)
        dac = max_subarray_dac(arr)
        kad = max_subarray_kadane(arr)
        print(f"Array {name}:")
        print(f"  Brute Force   -> Max Sum: {bf[0]}, Indices: ({bf[1]}, {bf[2]})")
        print(f"  Divide & Conc -> Max Sum: {dac[0]}, Indices: ({dac[1]}, {dac[2]})")
        print(f"  Kadane's      -> Max Sum: {kad[0]}, Indices: ({kad[1]}, {kad[2]})")
        print()

    # Benchmark Sizes
    sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    bf_times = []
    dac_times = []
    kad_times = []
    
    import random
    random.seed(42)
    
    print("--- RUNNING BENCHMARKS ---")
    for n in sizes:
        arr = [random.randint(-50, 50) for _ in range(n)]
        
        # Brute Force (skip for very large n to avoid excessive wait times)
        if n <= 10000:
            start_time = time.perf_counter()
            max_subarray_brute_force(arr)
            bf_times.append(time.perf_counter() - start_time)
        else:
            bf_times.append(None)
            
        # Divide and Conquer
        if n <= 50000:
            start_time = time.perf_counter()
            max_subarray_dac(arr)
            dac_times.append(time.perf_counter() - start_time)
        else:
            dac_times.append(None)
            
        # Kadane's Algorithm
        start_time = time.perf_counter()
        max_subarray_kadane(arr)
        kad_times.append(time.perf_counter() - start_time)
        
        print(f"Completed size n = {n}")

    # Plotting Results
    plt.figure(figsize=(10, 6))
    
    valid_bf_sizes = [sizes[i] for i, t in enumerate(bf_times) if t is not None]
    valid_bf_times = [t for t in bf_times if t is not None]
    
    valid_dac_sizes = [sizes[i] for i, t in enumerate(dac_times) if t is not None]
    valid_dac_times = [t for t in dac_times if t is not None]
    
    plt.plot(valid_bf_sizes, valid_bf_times, label="Brute Force $\Theta(n^2)$", marker='o')
    plt.plot(valid_dac_sizes, valid_dac_times, label="Divide & Conquer $\Theta(n \log n)$", marker='s')
    plt.plot(sizes, kad_times, label="Kadane's $\Theta(n)$", marker='^')
    
    plt.xlabel("Problem Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison of Maximum Subarray Algorithms")
    plt.legend()
    plt.grid(True)
    _script_dir = __import__('os').path.dirname(__import__('os').path.abspath(__file__))
    plt.savefig(__import__('os').path.join(_script_dir, "max_subarray_performance.png"))
    plt.show()