from app import app
from flask import redirect, session
from scripts.object_util import to_json
from scripts.order_util import get_order
from scripts.product_util import get_discounted_price
from scripts.session_util import validate_session
from template_renderer import render_template
import json

@app.route("/order/<order_id>")
def order(order_id = 0):
	user = validate_session(session)
	if not user:
		return redirect("/login/") # TODO: Error?

	try:
		order_id = int(order_id)
		assert(order_id > 0)
	except:
		return redirect("/cart/") # TODO: Error

	order = get_order(order_id)
	if order is None:
		return redirect("/cart/") # TODO: Error

	if order.cart.user_id != user.id:
		return redirect("/cart/") # TODO: Error

	item_prices = {} # Get prices at the time of order
	for item in order.cart.items:
		product = item.product

		item_prices[product.id] = get_discounted_price(product.id, order.timestamp)

	return render_template(
		"order.html",

		order_number = order_id,
		order_data = to_json(order),
		order_items = to_json(order.cart.items),
		item_prices = json.dumps(item_prices)
	)
