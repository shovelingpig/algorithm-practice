nums = [int(i) for i in input().split()]

isAsc = True
isDesc = True

for i in range(1, len(nums)):
    if nums[i-1] > nums[i]: isAsc = False
    else: isDesc = False

if isAsc: print('ascending')
elif isDesc: print('descending')
else: print('mixed')