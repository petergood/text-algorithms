def get_matching_positions(text, delta):
	res = []
	q = 0
	for s in range(0, len(text)):
		if (text[s] not in delta[q]):
			q = 0
			continue

		q = delta[q][text[s]]
		if (q == len(delta) - 1):
			res.append(s + 1 - q)
	return res

def get_delta(pattern):
	res = []
	letters = set()
	for c in pattern:
		letters.add(c)

	for q in range(0, len(pattern) + 1):
		res.append({})
		for c in letters:
			k = min(len(pattern) + 1, q + 2)
			while k > 0:
				k = k - 1
				if (pattern[0:k] == pattern[(q - k + 1):q] + c):
					break
			res[q][c] = k

	return res

def compare(text, pattern):
	return get_matching_positions(text, get_delta(pattern))