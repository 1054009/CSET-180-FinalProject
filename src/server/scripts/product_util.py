from database_session import database_session
from models import Product
from scripts.time_util import get_current_time, time_to_timestamp, timestamp_to_time

def get_products():
	return database_session.query(Product).all()

def get_product(id):
	try:
		return database_session.query(Product)					\
								.filter(Product.id == id)		\
								.first()
	except:
		return None

def get_price(id):
	product = get_product(id)

	if product is None:
		return 0

	return float(product.price) # Decimals suck

def get_discounted_price(id, timestamp = None):
	product = get_product(id)

	if product is None:
		return 0

	current_time = timestamp or get_current_time()

	total_discount = 0
	for discount in product.discounts:
		start_time = timestamp_to_time(discount.start_time)
		end_time = timestamp_to_time(discount.end_time)

		if start_time >= current_time and end_time <= current_time:
			total_discount += discount.percentage

	base_price = get_price(product.id)
	discount_amount = base_price * (total_discount / 100)

	return base_price - discount_amount
