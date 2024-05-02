import collections.abc
import json

PRIMITIVES = (
	bool,
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

	properties = dir(object)

	data = {}

	for property in properties:
		if property.startswith("_"): continue
		if not property in INDEX_PROPERTIES: continue

		property_value = getattr(object, property)
		if callable(property_value): continue

		if is_primitive(property_value): # Bloody strings count as sequences
			data[property] = to_json(property_value)
			continue

		if isinstance(property_value, collections.abc.Sequence): continue # TODO: Arrays and such

		data[property] = to_json(property_value)

	return json.dumps(data)
