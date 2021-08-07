# 나의 풀이
def solution(clothes):
    cloth_dict = {}
    
    for cloth in clothes:
        cloth_type = cloth[1]
        print(cloth_type)
        if cloth_type in cloth_dict:
            cloth_dict[cloth_type] += 1
        else:
            cloth_dict[cloth_type] = 1
    
    answer = 1
    for cloth_type in cloth_dict:
        answer *= (cloth_dict[cloth_type]+1)
    answer -= 1
    
    return answer
     
     
# 다른 풀이 1
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1

"""
# 한줄평
- 가장 Pythonic한 한줄짜리 코드였던 것 같다. Python의 lambda 함수와 list comprehension을 이용하면 코드를 굉장히 짧게 만들 수 있는 것 같다. 하지만 가독성 좋은 것은 아닌 것 같다. 
"""
