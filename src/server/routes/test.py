from app import app
from flask import render_template

from models import User, Customer, Vendor, Admin, Product, ProductImage, ProductDiscount, AvailableWarranty, ActiveWarranty
from session import database

from scripts.user_util import create_user, register_customer

from datetime import datetime

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

	test_customer = register_customer(test_user)

	print(test_customer.id)

	vendor_user = User(
		username = "mrdude",
		first_name = "Brandon",
		last_name = "Smith",
		email_address = "afagafsf@gmail.com",
		password = "hisafe".encode("utf-8")
	)

	database.add_all([ vendor_user ])
	database.flush()

	vendor_vendor = Vendor(
		user_id = vendor_user.id
	)

	database.add(vendor_vendor)
	database.flush()

	spoon = Product(
		name = "Big Spoon",
		description = "It is a comically large spoon",
		vendor_id = vendor_vendor.id,
		inventory = 5,
		price = 3.25
	)

	database.add(spoon)
	database.flush()

	spoon_warranty = AvailableWarranty(
		product_id = spoon.id,
		coverage_days = 50
	)

	database.add(spoon_warranty)
	database.flush()

	users_spoon_warranty = ActiveWarranty(
		warranty_id = spoon_warranty.id,
		user_id = test_user.id,
		activation_time = str(datetime.now())
	)

	database.add(users_spoon_warranty)
	database.flush()

	test_user.warranties.append(users_spoon_warranty)
	database.commit()

	return render_template("base.html")
