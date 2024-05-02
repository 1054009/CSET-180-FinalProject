import hashlib

def sha_string(string):
	return hashlib.sha256(string.encode("utf-8")).hexdigest()

def verify_password(user, password):
	stored_password = user.password.decode("utf-8")

	return stored_password == password or stored_password == sha_string(password)
