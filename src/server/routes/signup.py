from app import app
from flask import render_template, session

@app.route("/signup/")
def signup():
	session.clear()

	return render_template(
		"signup.html",

		no_footer = True
	)
