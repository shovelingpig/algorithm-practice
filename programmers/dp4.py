# 나의 풀이
def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대
    

# 다른 풀이 1
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, z2)
    
"""
# 한줄평
- 초기화에서는 첫 번째 집을 선택했을 경우, 두 번째는 선택하지 않은 경우 그 후 반복문에서는 x와 y 중 더 큰 값에 i 의 값을 더한 후에 x, y 값을 y, z 값으로 초기화 해주는 방식입니다.
"""
