# 나의 풀이
def solution(progresses, speeds):
    answer = []
    
    days = []
    
    for progress, speed in zip(progresses, speeds):
        if (100 - progress) % speed == 0:
            day = (100 - progress) // speed
        else:
            day = ((100 - progress) // speed) + 1
        days.append(day)
        
    stack = [days[0]]
    for day in days[1:]:
        if stack[0] >= day:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack = [day]
    answer.append(len(stack))
    
    return answer


# 다른 풀이 1
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

"""
# 한줄평
- -((p-100)//s)와 같이 음수의 내림을 이용해 양수의 올림을 구현함으로써 math.ceil()과 같은 외부 라이브러리를 이용하지 않은 점이 인상깊었다.
"""

    
# 다른 풀이 2
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

"""
# 한줄평
- 문제에서 제시된 상황을 가장 잘 이해하고 구현한 코드였고, 그렇기 때문에 자연스럽게 가독성이 높았다.
"""
