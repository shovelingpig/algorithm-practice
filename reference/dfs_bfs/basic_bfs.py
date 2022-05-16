from collections import deque


def bfs(adj_list, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v)

        for i in adj_list[v]:
            if not visited[i]:
                queue.append(i)
                visited[v] = True


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

bfs(adj_list, 1, visited)
