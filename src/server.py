# Imports
import platform
import os

from flask import Flask, render_template
from sqlalchemy import create_engine, text

IS_DEBUG = platform.system() == "Windows"

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

# Useful functions
def run_query(query, parameters = None):
	return sql.execute(text(query), parameters)

# Routes
@app.route("/")
def test():
	return render_template("base.html")

# Brap you
if IS_DEBUG and __name__ == "__main__":
 	app.run()
