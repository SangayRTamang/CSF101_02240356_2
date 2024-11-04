import matplotlib.pyplot as plt
import matplotlib.animation as animation
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr, threshold=10):
    # If array length is below threshold, use insertion sort in-place
    if len(arr) <= threshold:
        insertion_sort(arr, 0, len(arr) - 1)
        return arr

    # Otherwise, proceed with merge sort
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)
    
    # Merge left and right parts
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the hybrid Merge Sort
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = hybrid_merge_sort(test_arr)
print("Hybrid Merge Sort Result:", sorted_arr)


def bubble_sort_visual(arr):
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color='skyblue')
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) * 1.1)

    def update_bars(arr_data):
        for rect, val in zip(bar_rects, arr_data):
            rect.set_height(val)

    def bubble_sort_gen(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                yield arr.copy() 
            if not swapped:
                break

    ani = animation.FuncAnimation(fig, update_bars, frames=bubble_sort_gen(arr.copy()), repeat=False, blit=False)
    plt.show()

# Test the Bubble Sort visualization
test_arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_visual(test_arr)
