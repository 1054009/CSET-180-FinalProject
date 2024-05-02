from app import app
from database_session import database_session
from datetime import datetime
from models import User, Customer, Vendor, Admin, Product, ProductImage, ProductDiscount, AvailableWarranty, ActiveWarranty
from scripts.object_util import to_json
from scripts.user_util import create_user, register_customer, get_user_by_username
from template_renderer import render_template

@app.route("/test/")
def test():
	# test_user = User(
	# 	username = "jdog123",
	# 	first_name = "James",
	# 	last_name = "Douglas",
	# 	email_address = "jd123@gmail.com",
	# 	password = "awesomesecure456".encode("utf-8")
	# )

	test_user = create_user(
		username = "jdog123",
		first_name = "James",
		last_name = "Douglas",
		email_address = "jd123@gmail.com",
		hashed_password = "awesomesecure456"
	)

	print(to_json(test_user))

	test_customer = register_customer(test_user)

	print(test_user.as_customer())
	print(test_user.as_customer().as_user())
	print(test_user.as_vendor())
	print(test_user.as_admin())

	print(test_customer.id)

	vendor_user = User(
		username = "mrdude",
		first_name = "Brandon",
		last_name = "Smith",
		email_address = "afagafsf@gmail.com",
		password = "hisafe".encode("utf-8")
	)

	database_session.add_all([ vendor_user ])
	database_session.flush()

	vendor_vendor = Vendor(
		user_id = vendor_user.id
	)

	database_session.add(vendor_vendor)
	database_session.flush()

	spoon = Product(
		name = "Big Spoon",
		description = "It is a comically large spoon",
		vendor_id = vendor_vendor.id,
		inventory = 5,
		price = 3.25
	)

	database_session.add(spoon)
	database_session.flush()

	print(spoon.vendor)

	spoon_warranty = AvailableWarranty(
		product_id = spoon.id,
		coverage_days = 50
	)

	database_session.add(spoon_warranty)
	database_session.flush()

	users_spoon_warranty = ActiveWarranty(
		warranty_id = spoon_warranty.id,
		user_id = test_user.id,
		activation_time = str(datetime.now())
	)

	database_session.add(users_spoon_warranty)
	database_session.flush()

	test_user.warranties.append(users_spoon_warranty)
	database_session.commit()

	print(get_user_by_username(test_user.username))

	return render_template("base.html")
