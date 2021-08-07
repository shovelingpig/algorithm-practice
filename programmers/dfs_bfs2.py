# 나의 풀이
def recursive(node, is_checked, computers):
    is_checked[node] = 1
    
    for i in range(len(is_checked)):
        if (not is_checked[i]) and (computers[i][node] == 1):
            recursive(i, is_checked, computers)
            
def solution(n, computers):
    answer = 0
    is_checked = [0] * n
    
    for i in range(n):
        if not is_checked[i]:
            recursive(i, is_checked, computers)   
            answer += 1
    
    return answer

"""
# 한줄평
- 사용할 알고리즘을 먼저 생각나는대로 예시와 함께 주석으로 적어두니 구현하기가 훨씬 수월했고 코너 케이스를 처리하기 편했다. 앞으로도 처음에 글로 브레인스토밍하는 것을 연습하자.
"""


# 다른 풀이 1
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))
   
"""
# 한줄평
- 같은 네트워크에 있는 노드는 같은 숫자로 치환시키는 Floyd-Warshall 알고리즘을 이용한 방법이다. 재귀를 사용하지 않고 깔끔하게 구현하는 방법인 것 같다. 단 시간복잡도가 O(n^3)이라는 점을 주의해야한다.
"""


# 다른 풀이 2
def solution(n, computers):    
    def BFS(node, visit):
        que = [node]
        visit[node] = 1
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    visit = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        try:
            visit = BFS(visit.index(0), visit)
            answer += 1
        except:
            break
    return answer

"""
# 한줄평
- queue 자료구조를 이용한 BFS 알고리즘이다. 나도 재귀 함수 대신 queue나 stack을 이용한 그래프 탐색 방법을 더 연습해봐야겠다. 예외가 발생할 수 있는 부분을 try-except 문으로 처리해준 점이 인상깊었다.
"""
