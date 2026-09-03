#does the bisection as goes unlike merge.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Example usage
numbers = [64, 25, 12, 22, 11]
print(quick_sort(numbers))  # [11, 12, 22, 25, 64]