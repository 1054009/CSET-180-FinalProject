from app import app
from database_session import database_session
from models import Product, ProductImage, ProductDiscount
from template_renderer import render_template
from scripts.object_util import objects_as_json

@app.route("/products/")
def products():
	product_list = objects_as_json(Product)

	return render_template(
		"products.html",

		product_list = product_list
	)
