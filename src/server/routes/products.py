from app import app
from flask import request, redirect, session
from models import Product, ProductImage, ProductDiscount
from scripts.cart_util import add_to_cart
from scripts.object_util import objects_as_json
from scripts.session_util import validate_session
from template_renderer import render_template

@app.route("/products/")
def products_get():
	product_list = objects_as_json(Product)

	return render_template(
		"products.html",

		product_list = product_list
	)

@app.route("/products/add_to_cart/", methods = [ "POST" ])
def products_post():
	user = validate_session(session)
	if not user:
		return redirect("/products/") # TODO: Error

	product_id = request.form.get("product_id")
	if product_id is None:
		return redirect("/products/") # TODO: Error

	success = add_to_cart(user.email_address, product_id)
	# TODO: Show message depending on success

	return redirect("/products/")
