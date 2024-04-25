from flask import render_template

from models import User, Customer, Vendor, Admin, Product, ProductImage, ProductDiscount, AvailableWarranty, ActiveWarranty
from session import session

from datetime import datetime

@app.route("/test/")
def test():
	test_user = User(
		username = "jdog123",
		first_name = "James",
		last_name = "Douglas",
		email_address = "jd123@gmail.com",
		password = "awesomesecure456".encode("utf-8")
	)

	vendor_user = User(
		username = "mrdude",
		first_name = "Brandon",
		last_name = "Smith",
		email_address = "afagafsf@gmail.com",
		password = "hisafe".encode("utf-8")
	)

	session.add_all([ test_user, vendor_user ])
	session.flush()

	vendor_vendor = Vendor(
		user_id = vendor_user.id
	)

	session.add(vendor_vendor)
	session.flush()

	spoon = Product(
		name = "Big Spoon",
		description = "It is a comically large spoon",
		vendor_id = vendor_vendor.id,
		inventory = 5,
		price = 3.25
	)

	session.add(spoon)
	session.flush()

	spoon_warranty = AvailableWarranty(
		product_id = spoon.id,
		coverage_days = 50
	)

	session.add(spoon_warranty)
	session.flush()

	users_spoon_warranty = ActiveWarranty(
		warranty_id = spoon_warranty.id,
		user_id = test_user.id,
		activation_time = str(datetime.now())
	)

	session.add(users_spoon_warranty)
	session.flush()

	test_user.warranties.append(users_spoon_warranty)
	session.commit()

	return render_template("base.html")
