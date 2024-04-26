from models import User, Customer, Vendor, Admin, Product, ProductImage, ProductDiscount, AvailableWarranty, ActiveWarranty
from session import database

def create_user(username, first_name, last_name, email_address, hashed_password):
	try:
		new_user = User(
			username = username,
			first_name = first_name,
			last_name = last_name,
			email_address = email_address,
			password = hashed_password.encode("utf-8")
		)

		database.add(new_user)
		database.flush()

		return new_user
	except:
		return None

def register_customer(user):
	try:
		new_customer = Customer(
			user_id = user.id
		)

		database.add(new_customer)
		database.flush()

		return new_customer
	except:
		return None

def register_vendor(user):
	try:
		new_vendor = Vendor(
			user_id = user.id
		)

		database.add(new_vendor)
		database.flush()

		return new_vendor
	except:
		return None

def register_admin(user):
	try:
		new_admin = Admin(
			user_id = user.id
		)

		database.add(new_admin)
		database.flush()

		return new_admin
	except:
		return None
