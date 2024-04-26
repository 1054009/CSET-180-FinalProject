from models import User, Customer, Vendor, Admin, Product, ProductImage, ProductDiscount, AvailableWarranty, ActiveWarranty
from session import database

def create_user(username, first_name, last_name, email_address, hashed_password):
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

def register_customer(user):
	new_customer = Customer(
		user_id = user.id
	)

	database.add(new_customer)
	database.flush()

	return new_customer

def register_vendor(user):
	new_vendor = Vendor(
		user_id = user.id
	)

	database.add(new_vendor)
	database.flush()

	return new_vendor

def register_admin(user):
	new_admin = Admin(
		user_id = user.id
	)

	database.add(new_admin)
	database.flush()

	return new_admin
