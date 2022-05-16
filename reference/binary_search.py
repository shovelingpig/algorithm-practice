# O(logn)
def solve(arr, k, s, e):

    while e >= s:
        m = (s + e) // 2
        if arr[m] == k:
            return m + 1
        if arr[m] < k:
            s = m + 1
        else:
            e = m - 1

    return -1
