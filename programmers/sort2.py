# 나의 풀이
def solution(numbers):
    return "0" if all([n == 0 for n in numbers]) else ''.join(sorted([str(n) for n in numbers], key=lambda s:s*3, reverse=True))

"""
# 한줄평
- numbers의 모든 숫자가 0인 경우가 핵심 코너 케이스였다. 이때 0000...이 아닌 0을 리턴했어야 하는데 이를 생각하는데 시간이 오래 걸렸다.
"""


# 다른 풀이 1
def solution(numbers):
    return  str(int(''.join(sorted([str(n) for n in numbers], key=lambda s:s*3, reverse=True))))

"""
# 한줄평
- 내가 고민했던 코너 케이스를 더욱 아름답게 풀어낸 풀이이다. 문자열 0000...을 정수 0으로 바꾼 뒤 다시 문자열로 바꾸어주는 풀이이다.
"""


# 다른 풀이 2
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

"""
# 한줄평
- number가 100보다 작다는 제약조건을 이용하지 않고 풀 수 있는 comparator를 사용한 가장 정석적인 풀이이다. 두 원소의 우선순위를 비교할 때 a+b와 b+a를 비교한 점이 인상깊었다.
"""
