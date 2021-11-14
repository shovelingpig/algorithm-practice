###################
### my solution ###
###################

print(len(input().split()))


##########################
### another solution 1 ###
##########################

import sys

s = sys.stdin.read().strip()

if not s:
    print("0")
else:
    print(len(s.split(" ")))
    
"""
# 한줄평
- input() 함수는 느리다.
- sys.stdin의 readline() 함수 또는 read() 함수는 Buffer를 사용하기 때문에 더 빠르다.
- sys.stdin은 개행문자까지 입력되니 strip() 함수나 rstrip() 함수로 제거해야 한다.

# 참고문헌
https://developeryuseon.tistory.com/90
"""
