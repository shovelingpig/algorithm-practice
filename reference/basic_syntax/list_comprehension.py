# 2d list initialization
l = [[0 for _ in range(5)] for _ in range(5)]

# remove all
remove_set = {3, 5}
l = [i for i in l if i not in remove_set]