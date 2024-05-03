from database_session import database_session
from models import Product

def get_products():
	return database_session.query(Product).all()

def get_product(id):
	try:
		products = database_session.query(Product)

		return products.filter(Product.id == id).first()
	except:
		return None
