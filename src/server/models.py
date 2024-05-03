from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BLOB, LONGBLOB, DECIMAL, TEXT, TIMESTAMP, ENUM, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
	pass

class User(Base):
	__tablename__ = "users"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	username:Mapped[str] = mapped_column(
		VARCHAR(32),

		unique = True
	)

	first_name:Mapped[str] = mapped_column(
		VARCHAR(32)
	)

	last_name:Mapped[str] = mapped_column(
		VARCHAR(32)
	)

	email_address:Mapped[str] = mapped_column(
		VARCHAR(64),

		unique = True
	)

	password:Mapped[str] = mapped_column(
		BLOB
	)

	warranties = relationship(
		"ActiveWarranty",
		backref = "User"
	)

	carts = relationship(
		"Cart",
		backref = "User"
	)

	# Not sure on the best way to do these,,,
	customer = relationship(
		"Customer",
		backref = "User"
	)

	vendor = relationship(
		"Vendor",
		backref = "User"
	)

	admin = relationship(
		"Admin",
		backref = "User"
	)

	def as_customer(self):
		if len(self.customer) < 1:
			return None

		return self.customer[0]

	def as_vendor(self):
		if len(self.vendor) < 1:
			return None

		return self.vendor[0]

	def as_admin(self):
		if len(self.admin) < 1:
			return None

		return self.admin[0]

	def __repr__(self) -> str:
		return f"<User {self.email_address}>"

class Customer(Base):
	__tablename__ = "customers"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id"),

		unique = True
	)

	user = relationship(
		"User",
		backref = "Customer",
		viewonly = True
	)

	def as_user(self): # Why is this one different than the one above
		return self.user

	def __repr__(self) -> str:
		return f"<Customer {self.as_user().email_address}>"

class Vendor(Base):
	__tablename__ = "vendors"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id"),

		unique = True
	)

	user = relationship(
		"User",
		backref = "Vendor",
		viewonly = True
	)

	def as_user(self):
		return self.user

	def __repr__(self) -> str:
		return f"<Vendor {self.as_user().email_address}>"

class Admin(Base):
	__tablename__ = "admins"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id"),

		unique = True
	)

	user = relationship(
		"User",
		backref = "Admin",
		viewonly = True
	)

	def as_user(self):
		return self.user

	def __repr__(self) -> str:
		return f"<Admin {self.as_user().email_address}>"

class Product(Base):
	__tablename__ = "products"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	master_product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id"),

		nullable = True
	)

	name:Mapped[str] = mapped_column(
		VARCHAR(128)
	)

	description:Mapped[str] = mapped_column(
		VARCHAR(255),

		nullable = True
	)

	vendor_id:Mapped[int] = mapped_column(
		ForeignKey("vendors.id")
	)

	inventory:Mapped[int] = mapped_column(
		INTEGER(unsigned = True)
	)

	price:Mapped[float] = mapped_column(
		DECIMAL(8, 2, unsigned = True)
	)

	images = relationship(
		"ProductImage",
		backref = "Product"
	)

	discounts = relationship(
		"ProductDiscount",
		backref = "Product"
	)

	vendor = relationship(
		"Vendor",
		backref = "Product"
	)

	def get_vendor(self):
		return self.vendor

	def __repr__(self) -> str:
		return f"<Product {self.name}>"

class ProductImage(Base):
	__tablename__ = "product_images"

	ignoreme_entry_id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id")
	)

	image_data:Mapped[str] = mapped_column(
		LONGBLOB
	)

	def __repr__(self) -> str:
		return f"<ProductImage {self.ignoreme_entry_id}>"

class ProductDiscount(Base):
	__tablename__ = "product_discounts"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id")
	)

	percentage:Mapped[float] = mapped_column(
		DECIMAL(5, 2, unsigned = True)
	)

	start_time:Mapped[str] = mapped_column(
		TIMESTAMP
	)

	end_time:Mapped[str] = mapped_column(
		TIMESTAMP
	)

	def __repr__(self) -> str:
		return f"<ProductDiscount {self.id}>"

class AvailableWarranty(Base):
	__tablename__ = "available_warranty"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id")
	)

	coverage_days:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		nullable = True
	)

	coverage_information:Mapped[str] = mapped_column(
		TEXT,

		nullable = True
	)

	def __repr__(self) -> str:
		return f"<AvailableWarranty {self.id}>"

class ActiveWarranty(Base):
	__tablename__ = "active_warranty"

	ignoreme_entry_id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	warranty_id:Mapped[int] = mapped_column(
		ForeignKey("available_warranty.id")
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id")
	)

	activation_time:Mapped[str] = mapped_column(
		TIMESTAMP
	)

	expiration_time:Mapped[str] = mapped_column(
		TIMESTAMP,

		nullable = True
	)

	def __repr__(self) -> str:
		return f"<ActiveWarranty {self.id}>"

class Cart(Base):
	__tablename__ = "carts"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id")
	)

	items = relationship(
		"CartItem",
		backref = "Cart"
	)

	def __repr__(self) -> str:
		return f"<Cart {self.id}>"

class CartItem(Base):
	__tablename__ = "cart_items"

	ignoreme_entry_id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	cart_id:Mapped[int] = mapped_column(
		ForeignKey("carts.id")
	)

	product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id")
	)

	quantity:Mapped[int] = mapped_column(
		INTEGER(unsigned = True)
	)

	product = relationship(
		"Product",
		backref = "CartItem"
	)

	def __repr__(self) -> str:
		return f"<CartItem {self.ignoreme_entry_id}>"

class Order(Base):
	__tablename__ = "orders"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	cart_id:Mapped[int] = mapped_column(
		ForeignKey("carts.id")
	)

	timestamp:Mapped[str] = mapped_column(
		TIMESTAMP
	)

	price:Mapped[float] = mapped_column(
		DECIMAL(16, 2, unsigned = True)
	)

	status:Mapped[str] = mapped_column(
		ENUM("pending", "confirmed", "canceled", "shipped", "delivered")
	)

	def __repr__(self) -> str:
		return f"<Order {self.id}>"

class Complaint(Base):
	__tablename__ = "complaints"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id")
	)

	timestamp:Mapped[str] = mapped_column(
		TIMESTAMP
	)

	title:Mapped[str] = mapped_column(
		VARCHAR(255)
	)

	description:Mapped[str] = mapped_column(
		TEXT
	)

	status:Mapped[str] = mapped_column(
		ENUM("pending", "reviewed", "accepted", "declined")
	)

	images = relationship(
		"ComplaintImage",
		backref = "Complaint"
	)

	def __repr__(self) -> str:
		return f"<Complaint {self.id}>"

class ComplaintImage(Base):
	__tablename__ = "complaint_images"

	ignoreme_entry_id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	complaint_id:Mapped[int] = mapped_column(
		ForeignKey("complaints.id")
	)

	image_data:Mapped[str] = mapped_column(
		LONGBLOB
	)

	def __repr__(self) -> str:
		return f"<ComplaintImage {self.ignoreme_entry_id}>"

class Review(Base):
	__tablename__ = "reviews"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id")
	)

	timestamp:Mapped[str] = mapped_column(
		TIMESTAMP
	)

	rating:Mapped[int] = mapped_column(
		TINYINT
	)

	description:Mapped[str] = mapped_column(
		TEXT,

		nullable = True
	)

	images = relationship(
		"ReviewImage",
		backref = "Review"
	)

	def __repr__(self) -> str:
		return f"<Review {self.id}>"

class ReviewImage(Base):
	__tablename__ = "review_images"

	ignoreme_entry_id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	review_id:Mapped[int] = mapped_column(
		ForeignKey("reviews.id")
	)

	image_data:Mapped[str] = mapped_column(
		LONGBLOB
	)

	def __repr__(self) -> str:
		return f"<ReviewImage {self.ignoreme_entry_id}>"

# TODO: Maybe chats?
