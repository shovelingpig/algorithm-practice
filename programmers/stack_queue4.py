# 나의 풀이
def solution(prices):
    answer = []
    
    is_down = [0] * len(prices)
    
    for i in range(len(prices)):
        answer.append(0)
        
        for j in range(i):
            if not is_down[j]:
                if prices[j] > prices[i]:
                    answer[j] += 1
                    is_down[j] = 1
                else:
                    answer[j] += 1
    
    return answer


# 나의 풀이 2
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt = 0
        
        for j in range(i+1, len(prices)):
            pivot = prices[i]
            if prices[j] < pivot:
                cnt += 1
                break
            else:
                cnt += 1
                
        answer.append(cnt)
    
    return answer
    
"""
# 한줄평
- 반복을 최소화할 수 있는 방안을 찾으니 속도가 빨라졌다.
"""


# 다른 풀이 1
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

"""
# 한줄평
- stack을 이용하라는 문제의 취지에 가장 적합한 풀이한 것 같았다. stack에 넣어두었다가 가격이 떨어지는 지점에서 딱 한번만 기간을 계산해주는 점이 인상깊었다. O(n)이 가능한 수 있는 풀이인 것 같아 관심있게 보았다.
"""
