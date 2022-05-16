N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]


def dfs(x, y):
    # termination
    if (x <= -1) or (x >= N) or (y <= -1) or (y >= M):
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y) # left
        dfs(x, y - 1) # down
        dfs(x + 1, y) # right
        dfs(x, y + 1) # up

        return True

    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
