# 나의 풀이
import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        
        first_food = heapq.heappop(heap)
        second_food = heapq.heappop(heap)
        new_food = first_food + (second_food * 2)
        heapq.heappush(heap, new_food)
        answer += 1
    
    return answer

"""
# 한줄평
- 주어진 조건을 결과적으로 만족할 수 없어 -1을 반환해야하는 코너 케이스를 처리하는 것이 핵심이었다.
"""


"""
# 다른 풀이 1
(나중에 나온 mix값이 먼저 나온 것보다 클 수밖에 없어서 섞는 순서대로 queue에 넣어주면 크기 순서를 신경 쓸 필요가 없기 때문에 그냥 popleft로 꺼내면 무조건 mix값의 최소이다.)
"""
