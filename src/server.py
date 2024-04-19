# Imports
from pathlib import Path
import os
import platform

from flask import Flask, render_template
from sqlalchemy import create_engine, text

IS_DEBUG = platform.system() == "Windows"
EXECUTING_DIRECTORY = Path(__file__).parent.resolve()

# Initialize Flask
app = Flask(__name__)

# Connect to database
DB_USERNAME = "root"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_DB = "cset180final"

if not IS_DEBUG:
	DB_USERNAME = os.environ.get("FREEDB_USERNAME")
	DB_PASSWORD = os.environ.get("FREEDB_PASSWORD")
	DB_HOST = os.environ.get("FREEDB_HOST")
	DB_PORT = 3306
	DB_DB = os.environ.get("FREEDB_DB")

engine = create_engine(f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DB}")
sql = engine.connect()

# The rest
def load_file(path):
	path = (EXECUTING_DIRECTORY / path).resolve()

	try:
		file = open(path)

		exec(file.read())

		file.close()
	except:
		pass

load_file("./scripts/util.py")
load_file("./scripts/routes.py")

# Brap you
if IS_DEBUG and __name__ == "__main__":
 	app.run()
