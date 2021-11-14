###################
### my solution ###
###################

word = input().upper()

dict = {}
for c in word:
    if c not in dict.keys():
        dict[c] = 1
    else:
        dict[c] += 1
        
rank = sorted(dict.items(), key=lambda x: x[1], reverse=True)

if len(rank) != 1 and rank[0][1] == rank[1][1]:
    print("?")
else:
    print(rank[0][0])


##########################
### another solution 1 ###
##########################

s, a = input().lower(), []
for i in range(97, 123):
    a.append(s.count(chr(i)))
print('?' if a.count(max(a)) > 1 else chr(a.index(max(a)) + 97).upper())

"""
# 한줄평
- list의 count() 함수를 잘 활용한 것이 인상적이었다.
"""
