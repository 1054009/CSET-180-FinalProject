import flask

def render_template(template_name, **data):
	return flask.render_template(
		template_name,

		session = {
			"user_id": flask.session.get("user_id"),
			"email_address": flask.session.get("email_address"),
			"user_type": flask.session.get("user_type")
		},

		**data
	)
