# 10. Write a test program to implement Divide and Conquer Strategy. Eg: Quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [99,11,22,66,77,44,1,22,3]
sorted_list = quick_sort(my_list)

print("Sorted list:", sorted_list)
