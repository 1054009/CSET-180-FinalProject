from models import User, Customer, Vendor, Admin, Product, ProductImage, ProductDiscount, AvailableWarranty, ActiveWarranty
from database_session import database_session

def create_user(username, first_name, last_name, email_address, hashed_password):
	try:
		new_user = User(
			username = username,
			first_name = first_name,
			last_name = last_name,
			email_address = email_address,
			password = hashed_password.encode("utf-8")
		)

		database_session.add(new_user)
		database_session.commit()

		return new_user
	except:
		return None

def get_user_by_username(username):
	try:
		users = database_session.query(User)

		return users.filter(User.username == username).first()
	except:
		return None

def get_user_by_email(email_address):
	try:
		users = database_session.query(User)

		return users.filter(User.email_address == email_address).first()
	except:
		return None

def register_customer(user):
	try:
		new_customer = Customer(
			user_id = user.id
		)

		database_session.add(new_customer)
		database_session.commit()

		return new_customer
	except:
		return None

def register_vendor(user):
	try:
		new_vendor = Vendor(
			user_id = user.id
		)

		database_session.add(new_vendor)
		database_session.commit()

		return new_vendor
	except:
		return None

def register_admin(user):
	try:
		new_admin = Admin(
			user_id = user.id
		)

		database_session.add(new_admin)
		database_session.commit()

		return new_admin
	except:
		return None
