from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value) # index +1 of last element
    left_index = bisect_left(a, left_value) # index of first element
    return right_index - left_index


a = [1, 2, 3] 
print(count_by_range(a, 2, 3))
