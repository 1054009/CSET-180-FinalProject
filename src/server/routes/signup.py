from app import app
from flask import redirect, request, session
from scripts.password_util import sha_string
from scripts.user_util import create_user, get_user_by_username, get_user_by_email
from template_renderer import render_template

@app.route("/signup/")
def signup_get():
	session.clear()

	return render_template("signup.html")

@app.route("/signup/", methods = [ "POST" ])
def signup_post():
	session.clear()

	# Who needs to sanitize inputs when you have swag
	username = request.form.get("username", "stupid_idiot")
	first_name = request.form.get("first_name", "Stupid")
	last_name = request.form.get("last_name", "Idiot")
	email = request.form.get("email", "stupid@idiot.com")
	password = request.form.get("password", "stupididiot")

	existing = get_user_by_username(username)
	if existing is not None:
		return render_template(
			"signup.html",

			tooltip_element = "input[name=username]",
			tooltip_text = "A user with this name already exists",
			tooltip_direction = 2
		)

	existing = get_user_by_email(email)
	if existing is not None:
		return render_template(
			"signup.html",

			tooltip_element = "input[name=email]",
			tooltip_text = "A user with this email already exists",
			tooltip_direction = 2
		)

	create_user(
		username,
		first_name,
		last_name,
		email,
		sha_string(password)
	)

	return redirect("/login/")
