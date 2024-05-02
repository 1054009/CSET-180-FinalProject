from app import app
from database_session import database_session
from models import Product, ProductImage, ProductDiscount
from scripts.object_util import objects_as_json
from template_renderer import render_template

@app.route("/products/")
def products():
	product_list = objects_as_json(Product)
	product_images = objects_as_json(ProductImage)

	return render_template(
		"products.html",

		product_list = product_list,
		product_images = product_images
	)
