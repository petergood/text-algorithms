def compare(text, pattern):
	res = []
	for s in range(0, len(text) - len(pattern) + 1):
		if (pattern == text[s:(s + len(pattern))]):
			res.append(s)
	return res