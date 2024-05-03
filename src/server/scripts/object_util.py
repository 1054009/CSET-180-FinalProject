from database_session import database_session
from decimal import Decimal # ?? Floats ??
import collections.abc
import json

PRIMITIVES = (
	bool,
	Decimal,
	float,
	int,
	str,
	type(None)
)

# Horrible, botched way to do this
# Do not do it like this
INDEX_PROPERTIES = ( # TODO: Arrays and such
	# User
	"id",
	"username",
	"first_name",
	"last_name",
	"email_address",

	# Customer, Vendor, Admin
	"user_id",

	# Product
	"master_product_id",
	"name",
	"description",
	"vendor_id",
	"inventory",
	"price",

	# ProductImage
	"product_id",
	"image_data",

	# ProductDiscount
	"percentage",
	"start_time",
	"end_time",

	# AvailableWarranty
	"coverage_days",
	"coverage_information",

	# ActiveWarranty
	"warranty_id",
	"activation_time",
	"expiration_time",

	# Cart

	# CartItem
	"cart_id",
	"quantity",

	# Order
	"timestamp",
	"status",

	# Complaint
	"title",

	# ComplaintImage
	"complaint_id",

	# Review
	"rating",

	# ReviewImage
	"review_id"
)

def is_primitive(object):
	return isinstance(object, PRIMITIVES)

def to_json(object):
	if is_primitive(object):
		return str(object)

	if isinstance(object, collections.abc.Sequence): # Fix for when an array is passed in
		data = []

		for sub in object:
			data.append(to_json(sub))

		return json.dumps(data)

	data = {}

	for property in dir(object):
		if property.startswith("_"): continue
		if not property in INDEX_PROPERTIES: continue

		property_value = getattr(object, property)
		if callable(property_value): continue

		if isinstance(property_value, bytes): # Byte strings are stupid
			property_value = property_value.decode("utf-8")

		if is_primitive(property_value): # Bloody strings count as sequences
			data[property] = to_json(property_value)
			continue

		if isinstance(property_value, collections.abc.Sequence): continue # TODO: Arrays and such

		data[property] = to_json(property_value)

	return json.dumps(data)

def objects_as_json(type, filter_name = None, filter_value = None):
	objects = []

	query = database_session.query(type)

	if filter_name is not None:
		query = query.filter(getattr(type, filter_name) == filter_value)

	for object in query.all():
		objects.append(to_json(object))

	return json.dumps(objects)
