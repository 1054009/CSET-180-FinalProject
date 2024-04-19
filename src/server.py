# Imports
import platform
import os

from flask import Flask, render_template
from sqlalchemy import create_engine, text

# FreeDB information
FREEDB_USERNAME = os.environ.get("FREEDB_USERNAME")
FREEDB_PASSWORD = os.environ.get("FREEDB_PASSWORD")
FREEDB_HOST = os.environ.get("FREEDB_HOST")
FREEDB_PORT = 3306
FREEDB_DB = os.environ.get("FREEDB_DB")

# Setup Flask and connect to the database
app = Flask(__name__)
engine = create_engine(f"mysql://{FREEDB_USERNAME}:{FREEDB_PASSWORD}@{FREEDB_HOST}:{FREEDB_PORT}/{FREEDB_DB}")
sql = engine.connect()

def run_query(query, parameters = None):
	return sql.execute(text(query), parameters)

# Routes
@app.route("/")
def test():
	return render_template("base.html")

# Brap you
if platform.system() == "Windows" and __name__ == "__main__":
 	app.run()
