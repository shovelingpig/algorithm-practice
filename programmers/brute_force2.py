# 나의 풀이
import math

def solution(numbers):
    comb = []
    for n in numbers:
        recursive_search(n, list(numbers), '', comb)
    return sum([is_prime_num(c) for c in set(comb)])

def recursive_search(num, numbers, result_str, comb):
    result_str = result_str + num
    comb.append(int(result_str))
    numbers.remove(num)
    for n in numbers:
        recursive_search(n, numbers.copy(), result_str, comb)

def is_prime_num(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
    
    
# 다른 풀이 1
primeSet = set()

def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))
    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])

def solution(numbers):
    makeCombinations("", numbers)
    answer = len(primeSet)
    return answer

"""
# 한줄평
- 아래에서 위로 갈수록 점점 추상적인 함수에서 구체적인 함수로 선언하는 게 국룰인 것 같다. 나와 비슷한 재귀 알고리즘을 사용하였지만 훨씬 깔끔하게 구현한 것 같다.
"""


# 다른 풀이 2
from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

"""
# 한줄평
- itertools 라이브러리의 permutation 함수는 첫번째 인자로 온 리스트에서 두번째 인자로 온 숫자만큼을 뽑아 그 permutation들을 반환하는 함수다. 집합에서 |(OR)은 합집합 연산자다.
- 에라토스테네스 체를 set을 활용해서 구현한 알고리즘이다. 이 사람은 진짜 천재인가? ㅋㅋ
"""
