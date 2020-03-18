def compare(text, pattern):
    pi = build_prefix_array(pattern)
    q = 0
    res = []
    for i in range(0, len(text)):
        while (q > 0 and pattern[q] != text[i]):
            q = pi[q - 1]
        if (text[i] == pattern[q]):
            q = q + 1
        if (q == len(pattern)):
            res.append(i - q + 1)
            q = pi[q - 1]
    return res

def build_prefix_array(pattern):
    pi = [0]
    k = 0
    for q in range(1, len(pattern)):
        while (k > 0 and pattern[q] != pattern[k]):
            k = pi[k - 1]
        if (pattern[q] == pattern[k]):
            k = k + 1
        pi.append(k)
    return pi
