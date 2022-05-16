weights = []


def floyd_warshall(i, j, k):
    if k < 0:
        return weights[i][j]
    
    return min(floyd_warshall(i, j, k - 1), floyd_warshall(i, k, k - 1) + floyd_warshall(k, j, k - 1))
