from database_session import database_session
from models import Cart, CartItem, Order

def get_order(id):
	try:
		return database_session.query(Order)				\
								.filter(Order.id == id)		\
								.first()
	except:
		return None
