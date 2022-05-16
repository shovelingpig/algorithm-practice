def dfs(adj_list, v, visited):
    visited[v] = True
    print(v)

    for i in adj_list[v]:
        if not visited[i]:
            dfs(adj_list, i, visited)


adj_list = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(adj_list)

dfs(adj_list, 1, visited)
