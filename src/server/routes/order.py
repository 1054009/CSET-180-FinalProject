from app import app
from flask import redirect, session
from scripts.session_util import validate_session
from scripts.order_util import get_order
from template_renderer import render_template
from scripts.object_util import to_json

@app.route("/order/<order_id>")
def order(order_id = 0):
	user = validate_session(session)
	if not user:
		return redirect("/login/") # TODO: Error?

	try:
		order_id = int(order_id)
		assert(order_id > 0)
	except:
		print("bad id")

		return redirect("/cart/") # TODO: Error

	order = get_order(order_id)
	if order is None:
		print("not found")
		return redirect("/cart/") # TODO: Error

	if order.cart.user_id != user.id:
		print("bad user")
		return redirect("/cart/") # TODO: Error

	return render_template(
		"order.html",

		order_data = to_json(order),
		order_items = to_json(order.cart.items)
	)
