from itertools import permutations, combinations, product, combinations_with_replacement


data = ['A', 'B', 'C']

R = 2
# 순열: R개의 데이터를 뽑아 순서를 고려하여 나열하는 모든 경우
result1 = list(permutations(data, R))
# 조합: R개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우
result2 = list(combinations(data, R))
# 중복을 허용한 permutations
result3 = list(product(data, repeat=R))
# 중복을 허용한 combinations
result4 = list(combinations_with_replacement(data, R))
