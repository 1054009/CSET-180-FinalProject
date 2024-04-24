def sha256(string):
	return hashlib.sha256(string.encode("utf-8")).hexdigest()
