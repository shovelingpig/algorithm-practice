###################
### my solution ###
###################

a, b = input().split()
result = int(a) + int(b)
print(result)


##########################
### another solution 1 ###
##########################

print(sum(map(int, input().split())))

"""
# 한줄평
- list의 element 전체에 어떤 변환을 적용해야할 때에는 map 함수를 활용할 수 있다는 것을 배웠다.
"""
