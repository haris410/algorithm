# Write a program that accepts the vertices and edges for a graph and stores it as an adjacency matrix

num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

print("Enter edges (vertex1 vertex2):")
for _ in range(num_edges):
    v1, v2 = map(int, input().split())
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1  # For undirected graph

print("\nAdjacency Matrix:")
for row in adj_matrix:
    print(row)
