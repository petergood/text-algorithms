def longest_common_subsequence(x, y):
    m, n = len(x) + 1, len(y) + 1
    C = [[]] * m
    for i in range(m):
        C[i] = [0] * n

    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    
    i, j = m - 1, n - 1
    sigma = []

    while i > 0 and j > 0:
        if C[i][j] == C[i - 1][j - 1] + (1 if x[i - 1] == y[j - 1] else 0):
            if x[i - 1] == y[j - 1]:
                sigma.insert(0, x[i - 1])
            i = i - 1
            j = j - 1
        elif C[i][j] == C[i - 1][j]:
            i = i - 1
        else:
            j = j - 1

    return C[m - 1][n - 1], sigma