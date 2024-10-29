import time
import math

def linear_search_all(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i)
    return indices, comparisons

# Binary Search with Insertion Point Finder
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)
    comparisons = 0
    
    while left < right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left, comparisons  # Returns the insertion point and comparisons

# Jump Search
def jump_search(arr, target):
    length = len(arr)
    step = int(math.sqrt(length))
    prev = 0
    comparisons = 0
    
    # Finding the block where target may be present
    while arr[min(step, length)-1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1, comparisons
    
    # Linear search within the identified block
    while arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, length):
            return -1, comparisons
    
    # If element is found
    comparisons += 1
    if arr[prev] == target:
        return prev, comparisons
    
    return -1, comparisons

# Binary Search with Comparison Count
def binary_search_with_comparisons(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

# Comparison of different search algorithms
def compare_search_algorithms(arr, target):
    # Linear Search All Indices
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_all(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search with Comparisons (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search_with_comparisons(arr_sorted, target)
    binary_time = time.time() - start_time
    
    # Jump Search
    start_time = time.time()
    jump_result, jump_comparisons = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time

    print(f"Linear Search: Found at indices {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")

# Test with a sample list
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5

# Test Linear Search All Indices
indices, comparisons = linear_search_all(test_list, target)
print(f"Linear Search All Indices: Found target {target} at indices {indices} with {comparisons} comparisons")

# Test Binary Search Insertion Point
sorted_test_list = sorted(test_list)
insertion_point, comparisons = binary_search_insertion_point(sorted_test_list, target)
print(f"Binary Search Insertion Point: Target {target} should be inserted at index {insertion_point} with {comparisons} comparisons")

# Performance Comparison
compare_search_algorithms(list(range(1000)), 888)
