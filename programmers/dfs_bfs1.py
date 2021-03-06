# 나의 풀이
ANSWER = 0
TARGET = 0

def recursive(numbers, opr, result):
    numbers = numbers.copy()
    
    if opr == '+':
        result += numbers.pop()
    elif opr == '-':
        result -= numbers.pop()
    
    if numbers:
        recursive(numbers, '+', result)
        recursive(numbers, '-', result)
    else:
        global ANSWER
        global TARGET
        
        if result == TARGET:
            ANSWER += 1

def solution(numbers, target):
    global ANSWER
    global TARGET
    
    TARGET = target
    
    recursive(numbers, '+', 0)
    recursive(numbers, '-', 0)
    
    return ANSWER

"""
# 한줄평
- 재귀함수를 이용해 DFS를 구현했다. 다음에는 stack 자료구조를 활용해 구현해보고 싶다. python의 global variable 개념을 제대로 알게 된 좋은 기회였다.
"""


# 다른 풀이 1
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
 
"""
 # 한줄평
 - 분할정복을 사용한 점이 인상깊었다. list slicing을 하면 새로운 배열 객체가 만들어진다는 것을 새롭게 알았다. 재귀적으로 굉장히 아름다운 코드인 것 같다. 재귀 함수를 따로 만들지 않고 solution 함수 자체를 활용했고 종료 조건을 잘 명시했다.
"""

# 다른 풀이 2
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
    
"""
# 한줄평
- 재귀를 사용하지 않은 방법 중 제일 Pythonic한 것 같다. (x, -x) 쌍을 뽑아서 itertools 라이브러리의 product 연산을 취해주는 것이 정말 아름다운 방법이라고 생각했다.
"""
