import hashlib

def sha_string(string):
	return hashlib.sha256(string.encode("utf-8")).hexdigest()

def verify_password(user, password):
	return user.hashed_password == password or user.hashed_password == sha_string(password)
