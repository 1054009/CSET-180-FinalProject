from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BLOB, LONGBLOB, DECIMAL, TEXT, TIMESTAMP
from sqlalchemy import ForeignKey
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

		nullable = False,
		unique = True
	)

	first_name:Mapped[str] = mapped_column(
		VARCHAR(32),

		nullable = False
	)

	last_name:Mapped[str] = mapped_column(
		VARCHAR(32),

		nullable = False
	)

	email_address:Mapped[str] = mapped_column(
		VARCHAR(64),

		nullable = False,
		unique = True
	)

	password:Mapped[str] = mapped_column(
		BLOB,

		nullable = False
	)

	# # Relationships
	warranties = relationship(
		"ActiveWarranty",
		backref = "User"
	)

	# Overrides
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

		nullable = False
	)

class Vendor(Base):
	__tablename__ = "vendors"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id"),

		nullable = False
	)

class Admin(Base):
	__tablename__ = "admins"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id"),

		nullable = False
	)

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
		VARCHAR(128),

		nullable = False
	)

	description:Mapped[str] = mapped_column(
		VARCHAR(255),

		nullable = True
	)

	vendor_id:Mapped[int] = mapped_column(
		ForeignKey("vendors.id"),

		nullable = False
	)

	inventory:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		nullable = False
	)

	price:Mapped[float] = mapped_column(
		DECIMAL(8, 2, unsigned = True),

		nullable = False
	)

class ProductImage(Base):
	__tablename__ = "product_images"

	entry_id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True # This is only here because SQLAlchemy requires that tables have a primary key
	)

	product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id"),

		nullable = False
	)

	image_data:Mapped[str] = mapped_column(
		LONGBLOB,

		nullable = False
	)

class ProductDiscount(Base):
	__tablename__ = "product_discounts"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id"),

		nullable = False
	)

	percentage:Mapped[float] = mapped_column(
		DECIMAL(5, 2, unsigned = True),

		nullable = False
	)

	start_time:Mapped[str] = mapped_column(
		TIMESTAMP,

		nullable = False
	)

	end_times:Mapped[str] = mapped_column(
		TIMESTAMP
	)

class AvailableWarranty(Base):
	__tablename__ = "available_warranty"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	product_id:Mapped[int] = mapped_column(
		ForeignKey("products.id"),

		nullable = False
	)

	coverage_days:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		nullable = True
	)

	coverage_information:Mapped[str] = mapped_column(
		TEXT,

		nullable = True
	)

class ActiveWarranty(Base):
	__tablename__ = "active_warranty"

	entry_id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True # This is only here because SQLAlchemy requires that tables have a primary key
	)

	warranty_id:Mapped[int] = mapped_column(
		ForeignKey("available_warranty.id"),

		nullable = False
	)

	user_id:Mapped[int] = mapped_column(
		ForeignKey("users.id"),

		nullable = False
	)

	activation_time:Mapped[str] = mapped_column(
		TIMESTAMP,

		nullable = False
	)

	expiration_time:Mapped[str] = mapped_column(
		TIMESTAMP,

		nullable = True
	)

# class Fruit(Base):
# 	__tablename__ = "fruits"

# 	id:Mapped[int] = mapped_column(
# 		INTEGER(unsigned = True),

# 		primary_key = True
# 	)

# 	user_id:Mapped[int] = mapped_column(
# 		ForeignKey("users.id"),

# 		nullable = False
# 	)

# 	name:Mapped[str] = mapped_column(
# 		VARCHAR(32),

# 		nullable = False
# 	)

# 	# Relationships
# 	users:Mapped[List["User"]] = relationship(
# 		back_populates = "fruits"
# 	)

# 	# Overrides
# 	def __repr__(self) -> str:
# 		return f"<Fruit {self.name}>"
