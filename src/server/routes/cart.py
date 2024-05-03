from app import app
from flask import redirect, session
from scripts.cart_util import get_cart_items
from scripts.object_util import to_json
from scripts.session_util import validate_session
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

@app.route("/cart/", methods = [ "POST" ])
def cart_post():
	return redirect("/cart/")
