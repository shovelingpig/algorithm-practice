# Binary Search

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

left, right = 1, max(lans)
while left <= right:
    mid = (left + right) // 2
    n_lans = sum([lan // mid for lan in lans])
    if n_lans >= N: left = mid + 1
    else: right = mid - 1

print(right)