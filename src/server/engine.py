from os import environ
from platform import system
from sqlalchemy import create_engine

# Load environment data for database
if True:
	global SQL_USERNAME # Why can't you declare and set these all in 1 line :/
	global SQL_PASSWORD
	global SQL_HOST
	global SQL_PORT
	global SQL_DATABASE

	if system() == "Windows":
		SQL_USERNAME = "root"
		SQL_PASSWORD = "1234"
		SQL_HOST = "localhost"
		SQL_PORT = "3306"
		SQL_DATABASE = "cset180final"
	else:
		SQL_USERNAME = environ.get("FREEDB_USERNAME")
		SQL_PASSWORD = environ.get("FREEDB_PASSWORD")
		SQL_HOST = environ.get("FREEDB_HOST")
		SQL_PORT = "3306"
		SQL_DATABASE = environ.get("FREEDB_DB")

engine = create_engine(f"mysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DATABASE}")
sql = engine.connect()
