from app import app
from flask import render_template, redirect, request, session
from scripts.user_util import create_user, get_user_by_username, get_user_by_email
from scripts.password_util import sha_string

@app.route("/signup/")
def signup_get():
	session.clear()

	return render_template(
		"signup.html",

		no_footer = True
	)

@app.route("/signup/", methods = [ "POST" ])
def signup_post():
	session.clear()

	# Who needs to sanitize inputs when you have swag
	username = request.form.get("username", "stupid_idiot")
	first_name = request.form.get("first_name", "Stupid")
	last_name = request.form.get("last_name", "Idiot")
	email = request.form.get("email", "stupid@idiot.com")
	password = request.form.get("password", "stupididiot")

	existing = get_user_by_username(username) or get_user_by_email(email)
	if existing is not None:
		return redirect("/signup/") # TODO: Error

	create_user(
		username,
		first_name,
		last_name,
		email,
		sha_string(password)
	)

	return redirect("/login/")
