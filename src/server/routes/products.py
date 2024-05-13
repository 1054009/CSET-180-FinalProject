from app import app
from database_session import database_session
from decimal import Decimal
from flask import request, redirect, session
from models import Product, ProductImage, ProductDiscount
from scripts.cart_util import add_to_cart
from scripts.object_util import objects_as_json
from scripts.product_util import get_product
from scripts.session_util import validate_session
from template_renderer import render_template

@app.route("/products/")
def products_get():
	product_list = objects_as_json(Product)

	return render_template(
		"products.html",

		product_list = product_list
	)

@app.route("/products/edit/")
def products_edit_get():
	# TODO: Validate they have permission
	product_list = objects_as_json(Product)

	return render_template(
		"products.html",

		edit = True,
		product_list = product_list
	)

@app.route("/products/update/", methods = [ "POST" ])
def products_edit_post():
	product_id = request.form.get("product_id")
	if product_id is None:
		return redirect("/products/edit/") # TODO: Error

	product = get_product(product_id)
	if product is None:
		return redirect("/products/edit/") # TODO: Error

	# TODO: Make this more stable
	product.name = request.form.get("product_name", product.name)
	product.price = Decimal(request.form.get("product_price", product.price))
	product.description = request.form.get("product_description", product.description)

	database_session.commit()

	return redirect("/products/edit")

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
	# TODO: Handle cart amount going above available inventory

	return redirect("/products/")
