# Imports
import os
import pathlib
import platform
import secrets

import flask
import flask_sqlalchemy

# Constants
IS_DEBUG = platform.system() == "Windows"

SERVER_DIRECTORY = pathlib.Path(__file__).parent.resolve()
EXECUTING_DIRECTORY = SERVER_DIRECTORY

# Load environment data for database
if True:
	global SQL_USERNAME # Why can't you declare and set these all in 1 line :/
	global SQL_PASSWORD
	global SQL_HOST
	global SQL_PORT
	global SQL_DATABASE

	if IS_DEBUG:
		SQL_USERNAME = "root"
		SQL_PASSWORD = "1234"
		SQL_HOST = "localhost"
		SQL_PORT = "3306"
		SQL_DATABASE = "cset180final"
	else:
		environment = os.environ

		SQL_USERNAME = environment.get("FREEDB_USERNAME")
		SQL_PASSWORD = environment.get("FREEDB_PASSWORD")
		SQL_HOST = environment.get("FREEDB_HOST")
		SQL_PORT = "3306"
		SQL_DATABASE = environment.get("FREEDB_DB")

# Initialize Flask
app = flask.Flask(__name__)
config = app.config

config["DEBUG"] = True
config["SECRET_KEY"] = secrets.token_hex()
config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DATABASE}"

# Connect to database
sql = flask_sqlalchemy.SQLAlchemy(app)

# Include other files
def include(file_path):
	global EXECUTING_DIRECTORY
	executing_directory_backup = EXECUTING_DIRECTORY

	file_path = (EXECUTING_DIRECTORY / file_path).resolve()

	try:
		exec(open(file_path).read(), globals())
	except error:
		print(error)

	EXECUTING_DIRECTORY = executing_directory_backup

include("./scripts/imports.py")

# Run like normal if we're in debug
# gunicorn will be running it from the server end
if IS_DEBUG and __name__ == "__main__":
	app.run()
