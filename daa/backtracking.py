# Write a program to implement the backtracking algorithm for the sum of subsets problem.
def subset_sum(nums, target_sum, s=[], c=0):
    if c == target_sum: result.append(s[:])
    for i, num in enumerate(nums):
        subset_sum(nums[i+1:], target_sum, s + [num], c + num)

result = []
subset_sum([2, 4, 6, 8, 10], 16)
print("Subsets with sum equal to 16 are:", result)
