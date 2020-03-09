def compare(text, pattern):
	for s in range(0, len(text) - len(pattern) + 1):
		if (pattern == text[s:(s + len(pattern))]):
			return True
	return False