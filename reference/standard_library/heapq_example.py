import heapq


# min heap
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result


# max heap
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)
    
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    
    return result
