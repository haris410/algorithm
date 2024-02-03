# Write a program to Implement function to print In-Degree, Out-Degree, and to display the adjacency matrix.

MAX = 100
def indegree_outdegree(adj, n):
    in_degree = [0] * MAX
    out_degree = [0] * MAX

    for i in range(n):
        for j in range(n):
            in_degree[i] += adj[j][i]
            out_degree[i] += adj[i][j]

    for i in range(n):
        print(f"Vertex: {i+1} In-Degree: {in_degree[i]} Out-Degree: {out_degree[i]}")

    print("Adjacency matrix is:")
    for i in range(n):
        for j in range(n):
            print(adj[i][j], end=" ")
        print()

print("Enter the number of vertices:")
n = int(input())
print("Enter the adjacency matrix (1 for edge, 0 for no edge):")
adj = []
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)
indegree_outdegree(adj, n)
