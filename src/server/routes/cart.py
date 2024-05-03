from app import app
from flask import redirect, request
from template_renderer import render_template

@app.route("/cart/")
def cart_get():
	return render_template("cart.html")

@app.route("/cart/", methods = [ "POST" ])
def cart_post():
	return redirect("/cart/")
