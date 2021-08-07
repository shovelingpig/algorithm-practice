# 나의 풀이
MAX = 0

def solution(triangle):
    
    def dfs(layer, order, result):
        global MAX
        result += triangle[layer][order]            
        if layer == len(triangle) - 1:
            if result > MAX:
                MAX = result
            return
        for next_order in range(order, order+2):
            dfs(layer+1, next_order, result)
            
    global MAX
    dfs(0, 0, 0)
    return MAX

"""
# 한줄평
- 정확하지만 속도가 너무 느리다. 확인해보지 않아도 되는 경우를 제대로 걸러내지 못한 것 같다.
"""


# 다른 풀이 1
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j==i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])

"""
# 한줄평
- 재귀를 사용하지 않고 구현했다. 삼각형의 끝터리 부분과 안쪽 부분을 구별했고, 위의 값을 아래 값에 더해주는 과정을 반복하는 방식으로 문제를 해결하였다.
출처) https://codedrive.tistory.com/49
"""


# 다른 풀이 2
def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer

def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i,j)] = x

    return x
   
"""
# 한줄평
- 동적계획법의 Memoization 기법을 가장 잘 활용한 풀이 같다. 앞으로 나도 Memoization 기법을 구현할 때 구조를 잘 참고해야겠다.
"""


# 다른 풀이 3
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

"""
# 한줄평
1) 한 층씩 제거하며, 그 층에서 계산한 최대 이동거리 배열을 계산하여, 한 층을 제거한 traingle을 첫번째 input, 이동거리 배열을 두 번째 input으로 넣어줍니다.  
2) 따라서 traingle이 없으면 제거할 층이 없으므로 최종 조건입니다.  
3) [0] + l, l + [0] 을 이용하여 모서리 조건을 해결해줍니다. 
"""
