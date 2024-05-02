import hashlib

def sha_string(string):
	return hashlib.sha256(string.encode("utf-8")).hexdigest()

def verify_password(user, password):
	return user.password == password or user.password == sha_string(password)
