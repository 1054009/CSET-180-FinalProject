from typing import List

import sqlalchemy.dialects.mysql
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

	# Relationships
	fruits:Mapped[List["Fruit"]] = relationship(
		back_populates = "users"
	)

	# Overrides
	def __repr__(self) -> str:
		return f"<User {self.email_address}>"

class Fruit(Base):
	__tablename__ = "fruits"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	user_id:Mapped(int) = mapped_column(
		ForeignKey("users.id"),

		nullable = False
	)

	name:Mapped[str] = mapped_column(
		VARCHAR(32),

		nullable = False
	)

	# Relationships
	fruits:Mapped[List["User"]] = relationship(
		back_populates = "fruits"
	)

	# Overrides
	def __repr__(self) -> str:
		return f"<Fruit {self.name} owned by {self.user.email_address}>"
