from app import app
from flask import render_template, session

@app.route("/login/")
def login():
	session.clear()

	return render_template(
		"login.html",

		no_footer = True
	)
