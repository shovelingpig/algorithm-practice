# 나의 풀이
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    going_trucks = deque([0] * bridge_length)
    
    while truck_weights:
        t = truck_weights.pop(0)
        
        while True:
            going_trucks.pop()
            if sum(going_trucks) + t > weight:
                going_trucks.appendleft(0)
                answer += 1
            else:
                going_trucks.appendleft(t)
                answer += 1
                break
                
    answer += bridge_length
        
    return answer
    

# 다른 풀이 1
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    
    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    
    return time

"""
# 한줄평
- 0으로 초기화된 list를 * operator를 통해서 간단하게 마들 수 있다는 사실을 알았다. 이 문제는 deque보다 list를 썼을 때 더 빠르다는 사실이 당황스러웠다.
"""


# 다른 풀이 2
import collections

DUMMY_TRUCK = 0

class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()

"""
# 한줄평
- 클래스를 활용한 코드인데도 생각보다 너무 빨라서 놀랐다. 객체지향의 여러 장점들을 챙기면서도 속도까지 챙긴 코드라서 더욱 대단한 것 같다. 실무에서 가장 활용하고 싶은 형태의 코드이다.
"""
