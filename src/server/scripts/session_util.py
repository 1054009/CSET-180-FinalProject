from scripts.user_util import get_user_by_email

def validate_session(flask_session):
	email_user = get_user_by_email(flask_session.get("email_address"))
	if email_user is None:
		return False

	if email_user.id == flask_session.get("user_id"):
		return email_user
	else:
		return False
