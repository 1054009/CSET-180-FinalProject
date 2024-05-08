from app import app
from flask import redirect, session
from scripts.session_util import validate_session
from template_renderer import render_template

@app.route("/account/")
def account():
	user = validate_session(session)
	if not user:
		return redirect("/login/") # TODO: Error?

	return render_template(
		"account.html"
	)
