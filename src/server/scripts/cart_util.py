from database_session import database_session
from models import Product, ProductImage, ProductDiscount, Cart, Order
from scripts.user_util import get_user_by_email

def get_usable_carts(email_address):
	user = get_user_by_email(email_address)
	if user is None:
		return []

	return database_session.query(Cart)									\
							.outerjoin(Order, Cart.id == Order.cart_id)		\
							.filter(Order.cart_id is None)					\
							.order_by(Cart.id.desc())						\
							.all()

def create_cart(email_address):
	user = get_user_by_email(email_address)
	if user is None:
		return None

	cart = Cart(
		user_id = user.id
	)

	database_session.add(cart)
	database_session.commit()

	return cart
