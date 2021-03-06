# 나의 풀이
def solution(priorities, location):
    answer = 0
    cnt = 0
    
    while True:
        p = priorities.pop(0)
        max_p = max(priorities)
        
        if location - cnt == 0:
            if max_p > p:
                priorities.append(p)
                location = len(priorities) - 1
                cnt = 0
            else:
                answer += 1
                return answer
        else:
            if max_p > p:
                priorities.append(p)
                cnt += 1
            else:
                answer += 1
                cnt += 1
    
    return answer


# 다른 풀이 1
def solution(priorities, location):
    answer = 0

    array1 = [c for c in range(len(priorities))] # index 위치 저장 
    array2 = priorities.copy() # 값 저장 (출력되는 값)

    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            break

    return array1.index(location) + 1

"""
# 한줄평
- index의 위치를 저장하는 배열을 따로 만들고, array.append(array.pop(i))와 같이 이를 관리해주는 방식이 인상깊었다.
"""

    
# 다른 풀이 2
def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


# 다른 풀이 3
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

"""
# 한줄평
- enumerate 함수를 이용해 index와 value를 묶은 tuple을 만들어 index를 관리하는 점이 인상깊었다. 또한 stack과 queue를 구현할 때 list보다 훨씬 효율적인 deque라는 자료구조를 알게 되었다.
"""
