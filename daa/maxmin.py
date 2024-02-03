# Write a program to find minimum and maximum value in an array using divide and conquer.

def find_max_min(lst):
    if not lst:
        return None, None

    def helper(lst, start, end):
        if start == end:
            return lst[start], lst[start]

        mid = (start + end) // 2

        left_max, left_min = helper(lst, start, mid)
        right_max, right_min = helper(lst, mid + 1, end)

        return max(left_max, right_max), min(left_min, right_min)

    return helper(lst, 0, len(lst) - 1)

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_value, min_value = find_max_min(my_list)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
