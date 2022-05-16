from collections import deque, Counter, OrderedDict


# Deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
data.popleft()
data.pop()
print(list(data))

# Counter
counter = Counter(['R', 'B', 'R', 'G', 'B', 'B'])

print(counter['B'])
print(dict(counter))

# Deduplication with OrderedDict
a_str = 'aaaffggaahhaaaa'
print(''.join(OrderedDict.fromkeys(a_str))) # afgh
