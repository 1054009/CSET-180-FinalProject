from app import app
from flask import render_template
from database_session import database_session
from models import User, Product, Review

@app.route("/")
@app.route("/home/")
def home():
	user_count = database_session.query(User).count()
	product_count = database_session.query(Product).count()
	review_count = database_session.query(Review).count()

	return render_template(
		"home.html",

		user_count = user_count,
		product_count = product_count,
		review_count = review_count
	)
