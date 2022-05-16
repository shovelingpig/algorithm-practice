from collections import deque


N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

# direction
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로를 벗어난 겨우 무시
            if (nx < 0) or (ny < 0) or (nx >= N) or (ny >= M):
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 첫방문인 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[N - 1][M -1]


print(bfs(0, 0))
