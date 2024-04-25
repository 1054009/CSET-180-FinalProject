from typing import List

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BLOB, ENUM
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

	user_type:Mapped[str] = mapped_column(
		ENUM("customer", "vendor", "admin"),

		nullable = False
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
	# fruits:Mapped[List["Fruit"]] = relationship(
	# 	back_populates = "users"
	# )

	# Overrides
	def __repr__(self) -> str:
		return f"<User {self.email_address}>"

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
