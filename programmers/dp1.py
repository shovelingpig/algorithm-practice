# 나의 풀이
def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add( int(str(N) * i) )
        
        for j in range(0, i-1):
            for x in DP[j]:
                for y in DP[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break
        
        DP.append(numbers)

    return answer
    
"""
# 한줄평
- Memoization 기법을 이용했고 작은 수부터 반복문을 돌아서 효율성을 최대화하려고 노력했다. zero division error에 대한 코너 케이스에 주의해줘야 할 것 같다.
"""
