N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]

d = [10001] * (M+1)

# Bottom-up DP
d[0] = 0
for i in range(N):
    for j in range(arr[i], M + 1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
