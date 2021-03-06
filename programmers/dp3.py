# 나의 풀이
def solution(m, n, puddles):
    answers = [[0]*(m+1) for i in range(n+1)]
    answers[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if [j, i] in puddles:
                answers[i][j] == 0
            else:
                answers[i][j] = answers[i-1][j] + answers[i][j-1]
    return answers[n][m]%1000000007
    
"""
# 한줄평
- DP 문제는 최적부분구조를 찾는게 핵심인 것 같다. 이때 기존 사고의 역방향으로 생각해보는 것이 큰 도움이 된다. 이 문제에서는 계산의 편의를 위해 m+1개의 값이 0인 모서리 행과 n+1개의 값이 0인 모서리 열을 추가해줬다. puddles이 일반 행렬과 행과 열이 뒤집어져 있던 것이 함정이었다.
"""


# 다른 풀이 1
def solution(m, n, puddles):
    answer = 0
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007
    
"""
# 한줄평
- 재귀 함수를 이용했고, Dictionary를 활용한 Memoization을 통해 중복 계산을 막았다. Memoization에 Dictionary 자료구조가 아주 좋은 것 같다.
"""
