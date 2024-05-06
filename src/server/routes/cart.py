from app import app
from database_session import database_session
from flask import redirect, session
from models import CartItem, Order
from scripts.cart_util import get_best_cart, get_cart_items
from scripts.object_util import to_json
from scripts.product_util import get_discounted_price
from scripts.session_util import validate_session
from scripts.time_util import get_current_timestamp
from template_renderer import render_template

@app.route("/cart/")
def cart_get():
	user = validate_session(session)
	if not user:
		return redirect("/login/") # TODO: Error?

	cart_items = to_json(get_cart_items(user.email_address))

	return render_template(
		"cart.html",

		cart_items = cart_items
	)

@app.route("/cart/place_order", methods = [ "POST" ])
def cart_post():
	user = validate_session(session)
	if not user:
		return redirect("/login/") # TODO: Error?

	cart = get_best_cart(user.email_address)
	if cart is None:
		return redirect("/cart/") # TODO: Error

	items = database_session.query(CartItem)						\
							.filter(CartItem.cart_id == cart.id)	\
							.all() # Make sure there's stuff in the cart

	if len(items) < 1:
		return redirect("/cart/") # TODO: Error

	total_price = 0
	for item in items:
		total_price += get_discounted_price(item.product.id) * item.quantity

	order = Order(
		cart_id = cart.id,
		timestamp = get_current_timestamp(),
		price = total_price,
		status = "pending"
	)

	database_session.add(order)
	database_session.commit()

	return redirect(f"/order/{order.id}")
