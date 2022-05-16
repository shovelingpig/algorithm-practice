# O(n^2)
def bubble_sort(x):
	length = len(x)-1
	for i in range(length):
		for j in range(length-i):
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
	return x


# O(n^2)
def selection_sort(x):
	length = len(x)
	for i in range(length-1):
		for j in range(i+1, length):
			if x[i] > x[j]:
				x[i], x[j] = x[j], x[i]
	return x


# O(n^2), 최선의 경우 O(n)
def insertion_sort(x):
	for i in range(1, len(x)):
		j = i - 1
		key = x[i]
		while x[j] > key and j >= 0:
			x[j+1]  = x[j]
			j = j - 1
		x[j+1] = key
	return x


# O(nlogn), 최악의 경우 O(n^2)
def quick_sort(x):
	if len(x) <= 1:
		return x
 
	pivot = x[0]
	tail = x[1:]
	
	left = [x for x in tail if x <= pivot]
	right = [x for x in tail if x > pivot]

	return quicksort(left) + [pivot] + quicksort(right)


def quick_sort2(x, start, end):
	if start >= end:
		return
 
	pivot = start
	left = start + 1
	right = end

	while left <= right:

		while left <= end and x[left] <= x[pivot]:
			left += 1

		while right > start and x[right] >= x[pivot]:
			right -= 1

		if left > right:
			x[right], x[pivot] =  x[pivot], x[right]
		
		else:
			x[left], x[right] = x[right], x[left]
	
	quick_sort2(x, start, right - 1)
	quick_sort2(x, right + 1, end)


# O(nlogn)
def merge_sort(x):
	if len(x) <= 1:
		return x
 
	m = len(x) // 2
	L = mergeSort(x[:m])
	R = mergeSort(x[m:])
 
	result = []
	i = 0
	j = 0
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			result.append(L[i])
			i += 1
		else:
			result.append(R[j])
			j += 1
	result += L[i:]
	result += R[j:]
	return result


# O(n + k), k = max value
def counting_sort(x):
	count = [0] * (max(x) + 1)

	for i in range(len(x)):
		count[x[i]] += 1

	for i in range(len(count)):
		for j in range(count[i]):
			print(i, end=' ')
