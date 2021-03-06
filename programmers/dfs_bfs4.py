# 나의 풀이
ANSWER = []

def recursive(airport, tickets, path):
    global ANSWER
    
    if ANSWER:
        return
    
    path.append(airport)
    
    if len(tickets) == 0:
        ANSWER = path
        return
    
    for i in range(len(tickets)):
        src, des = tickets[i]
        if src == airport:
            recursive(des, tickets[:i] + tickets[i+1:], path.copy())
    
def solution(tickets):
    global ANSWER
    
    tickets.sort(key=lambda x: x[1])
    recursive('ICN', tickets, [])
    return ANSWER
    
"""
# 한줄평
- global variable을 사용한 것이 아쉽기는 하지만 문제의 본질은 잘 파악한 것 같다.
"""


# 다른 풀이 1
def solution(tickets):
    def helper(tickets, route):
        if tickets == []:
            return route
        left = [i for i in range(len(tickets)) if tickets[i][0] == route[-1]]
        if left == []:
            return None
        left.sort(key = lambda i: tickets[i][1])

        for next in left:
            rest = helper(tickets[:next]+tickets[next+1:], route+[tickets[next][1]])
            if rest is not None:
                return rest
    return helper(tickets, ["ICN"])

"""
# 한줄평
- 가장 깔끔한 풀이인 것 같다. 실패하는 탐색의 경우 result에 None을 할당하고, 최종 반환값을 정할 때는 None이 아닌 경우만 반환하도록 하는 점이 문제를 쉽게 해결한 열쇠인 것 같다. 하나의 재귀함수는 solution 함수 안에 선언하는 게 국룰인 것 같다.
"""
