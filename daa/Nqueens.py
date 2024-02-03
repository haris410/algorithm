# Write a program to implement backtracking algorithm for solving problems like Nqueens.
from itertools import permutations

def solve_nq(n):
    for queens in permutations(range(n)):  # Try all queen placements
        if all(abs(i - j) != abs(queens[i] - queens[j]) for i in range(n) for j in range(i + 1, n)):  # Check for conflicts
            return queens  # Solution found!
    return None  # No solution exists

if __name__ == "__main__":
    solution = solve_nq(4)
    if solution:
        print(solution)
    else:
        print("Solution does not exist")
