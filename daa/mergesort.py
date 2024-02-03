# 2. Write a program to implement Merge sort algorithm for sorting a list of integers in ascending order.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        arr[:] = merged

# Example usage:
my_list = [64, 25, 12, 22, 11]
merge_sort(my_list)

print("Sorted list:", my_list)
