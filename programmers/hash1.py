# 나의 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return (p)
    return participant.pop()


# 다른 풀이 1
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

"""
# 한줄평
- hash 함수를 이용하라는 문제의 취지에 가장 부합했던 풀이 같았다.
"""

    
# 다른 풀이 2
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

"""
# 한줄평
- collections 라이브러리의 Counter 객체에서 - operator가 하는 역할을 처음 알게 되었다.
"""
