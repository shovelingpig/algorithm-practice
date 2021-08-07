# 나의 풀이
def solution(answers):
    answer = []
    scores = [0] * 3
    
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1
    
    maximum = max(scores)
    for i in range(len(scores)):
        if scores[i] == maximum:
            answer.append(i+1)
    
    return answer
    

# 다른 풀이 1
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
    
# 한줄평
# itertools 라이브러리의 cycle 함수를 새롭게 알게 되었다. 최종 결과값을 만들 때 list comprehension을 쓴 것도 좋은 선택 같다.
