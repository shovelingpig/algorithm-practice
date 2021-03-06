# 나의 풀이
def solution(brown, yellow):
    a = 2
    b = - brown - 4
    c = 2*brown + 2*yellow
    
    D = b**2 - 4*a*c
    
    x1 = (- b + D**0.5) / (2*a)
    x2 = (brown + yellow) / x1
    
    return [max(x1, x2), min(x1, x2)]
    

# 다른 풀이 1
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

"""
# 한줄평
갈색 벽돌과 노란 벽돌의 관계식을 세워서 해당 식을 만족하는 정수해를 찾으면 되는데, 만족하는 식이 해당 정수의 곱으로 표현되니까 약수를 다 찾는 과정에서 range(1,sqrt(n))이 나온다.
"""
