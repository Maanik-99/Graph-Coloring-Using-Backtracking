def is_safe(node, graph, color, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def solve(node, graph, color, k, n):
    if node == n:
        return True

    for c in range(1, k + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if solve(node + 1, graph, color, k, n):
                return True
            color[node] = 0
    return False

def graph_coloring(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    n, m, k = map(int, lines[0].split())
    graph = [[] for _ in range(n)]
    for line in lines[1:]:
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * n
    if solve(0, graph, color, k, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", color)
    else:
        print(f"Coloring Not Possible with {k} Colors")

# Example usage
if __name__ == "__main__":
    graph_coloring("input.txt")
