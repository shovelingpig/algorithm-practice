# 나의 풀이
def solution(array, commands):
    return [sorted(array[c[0] - 1:c[1]])[c[2]-1] for c in commands]
    

# 다른 풀이 1
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

"""
# 한줄평
- 본질적인 알고리즘 자체는 비슷했다. 하지만 list comprehension 대신 map과 labmda함수의 조합을 사용할 수도 있다는 사실을 깨달았다. 하지만 list comprehension이 더 빠르다고 한다.
"""
