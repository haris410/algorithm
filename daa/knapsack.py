# Write program to implement Dynamic Programming algorithm for the 0/1 Knapsack problem

def knapsack(weights, profit, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + profit[i])

    return dp[capacity]

# Example usage with profit instead of values
weights = [10, 20, 30]
profit = [60, 100, 120]
capacity = 50

max_value = knapsack(weights, profit, capacity)
print("Maximum value:", max_value)
