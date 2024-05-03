from app import app
from flask import redirect, request, session
from scripts.password_util import verify_password
from scripts.user_util import get_user_by_username, get_user_by_email
from template_renderer import render_template

@app.route("/login/")
def login_get():
	session.clear()

	return render_template("login.html")

@app.route("/login/", methods = [ "POST" ])
def login_post():
	session.clear()

	login_name = request.form.get("login_name")
	password = request.form.get("password") # Not encrypted during transit :(

	user = get_user_by_username(login_name) or get_user_by_email(login_name)
	if user is None:
		return render_template(
			"login.html",

			tooltip_element = "input[name=login_name]",
			tooltip_text = "User not found",
			tooltip_direction = 2
		)

	if not verify_password(user, password):
		return render_template(
			"login.html",

			tooltip_element = "input[name=password]",
			tooltip_text = "Incorrect password entered",
			tooltip_direction = 2
		)

	session["user_id"] = user.id
	session["email_address"] = user.email_address

	return redirect("/products/")
