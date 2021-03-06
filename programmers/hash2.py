# 나의 풀이
def solution(phone_book):
    # sort
    phone_book.sort()
    
    # change type to string
    for idx, num in enumerate(phone_book):
        phone_book[idx] = str(num)
    
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    
    return True


# 다른 풀이 1
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

"""
# 한줄평
- list를 for in 문으로 순환할 때 list slicing을 적용하면 더 활용성이 높다는 것을 깨달았다.
"""


# 다른 풀이 2
def solution(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True

"""
# 한줄평
- 시간복잡도 상 가장 효율적인 코드 같았다.
"""


# 다른 풀이 3
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

"""
# 한줄평
- hash 함수를 이용하라는 문제의 취지에 가장 적합한 풀이 같았다.
"""
