# 나의 풀이
ANSWER = 0
ORIGINAL_LEN = 0
BEGIN = 0

def recursive(curr, target, words):
    global ANSWER
    global ORIGINAL_LEN
    global BEGIN
    
    if curr == target:
        new_answer = ORIGINAL_LEN - len(words) + 1
        if ANSWER > new_answer:
            ANSWER = new_answer
            return
    
    if curr != BEGIN:
        words.remove(curr)
    
    for word in words:
        if sum([word[i] != curr[i] for i in range(len(curr))]) == 1:
            recursive(word, target, words.copy())

def solution(begin, target, words):
    global ANSWER
    global ORIGINAL_LEN
    global BEGIN
    
    ANSWER = len(words)
    ORIGINAL_LEN = len(words)
    BEGIN = begin
    
    if target not in words:
        return 0
    
    recursive(begin, target, words)
    
    return ANSWER

"""
# 한줄평
- global varible을 안 쓰고 재귀 구조를 더 깔끔하게 구현했으면 좋았지 싶다.
"""


# 다른 풀이 1
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)

"""
# 한줄평
- queue 자료구조를 활용해 최단거리를 구하는 알고리즘을 사용하였다. get_adjacent 함수를 따로 구현한 것이 좋은 추상화의 예인 것 같다. yield 함수를 이용해 generator를 만들 수 있다는 사실을 처음 알았다.
"""


# 다른 풀이 2
def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1
 
"""
 # 한줄평
 - 이 풀이는 queue 자료구조를 가장 잘 활용한 풀이 같았다. word_1이 현재 관심의 대상인 단어이고, word_2는 다음 관심의 대상이 될 단어이다. zip() 함수와 list comprehension을 이용해 가독성을 높인 점도 인상깊었다.
"""     
        
