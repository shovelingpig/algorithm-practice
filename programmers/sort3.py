# 나의 풀이
def solution(citations):
    sorted_list = sorted(citations, reverse=True)
    for pivot in range(sorted_list[0], -1, -1):
        cnt = sum([pivot <= c for c in sorted_list])
        if cnt >= pivot:
            return pivot
 
"""
# 한줄평
- 처음에 for pivot in citations과 같은 반복문을 사용했다가 실패했다. 자신이 생각한 방법이 실패할 수 있는 코너 케이스에 대해서 생각해보는 것이 알고리즘 풀이에 아주 중요한 것 같다.
"""


# 다른 풀이 1
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

"""
# 한줄평
- 인용수와 논문수 중 낮은 값을 취하여 H-Index의 후보값 리스트를 만들고 그 리스트의 최대값을 구하는 방식이 인상깊었다. map(fun, list) 함수를 앞으로 애용해야겠다고 생각했고, enumerate 함수에 인자로 start를 설정해줄 수 있는지 처음 알았다.
"""


# 다른 풀이 2
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

"""
# 한줄평
- count를 구할 때 나처럼 sum 함수를 이용하지 않고 정렬한 후의 index를 이용했다. 내 풀이보다 훨씬 효율적인 방법인 것 같다.
"""
