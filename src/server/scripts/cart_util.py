from database_session import database_session
from models import Product, ProductImage, ProductDiscount, Cart, CartItem, Order
from scripts.product_util import get_product
from scripts.user_util import get_user_by_email

def get_usable_carts(email_address):
	user = get_user_by_email(email_address)
	if user is None:
		return []

	# Get all carts that are NOT part of an order
	# Once a cart is used for an order, it's considered locked
	return database_session.query(Cart)										\
							.outerjoin(Order, Cart.id == Order.cart_id)		\
							.filter(Order.cart_id is not None)				\
							.order_by(Cart.id.desc())						\
							.all() # TODO: Test this somehow

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

def get_best_cart(email_address):
	carts = get_usable_carts(email_address)

	if len(carts) < 1:
		return create_cart(email_address)
	else:
		return carts[0]

def add_to_cart(email_address, product_id):
	cart = get_best_cart(email_address)
	if cart is None:
		return False

	product = get_product(product_id)
	if product is None:
		return False

	for item in cart.items:
		if item.product_id == product.id:
			item.quantity += 1
			database_session.commit()

			return item

	item = CartItem(
		cart_id = cart.id,
		product_id = product.id,
		quantity = 1
	)

	database_session.add(item)
	database_session.commit()

	return item
