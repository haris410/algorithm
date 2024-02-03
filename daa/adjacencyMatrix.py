# Write a program that accepts the vertices and edges for a graph and stores it as an adjacency matrix

num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

print("Enter edges (vertex1 vertex2):")
for _ in range(num_edges):
    vertex1, vertex2 = map(int, input().split())
    adjacency_matrix[vertex1][vertex2] = 1
    adjacency_matrix[vertex2][vertex1] = 1  # For undirected graph

print("\nAdjacency Matrix:")
for row in adjacency_matrix:
    print(row)
