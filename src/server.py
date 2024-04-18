# Imports
import platform
from flask import Flask, render_template
from sqlalchemy import create_engine, engine_from_config, text

# FreeDB information
FREEDB_USERNAME = "freedb_1054009"
FREEDB_PASSWORD = "$hchYjtYar$BAh2" # pls don't hack kthx
FREEDB_HOST = "sql.freedb.tech"
FREEDB_PORT = 3306
FREEDB_DB = "freedb_cset180final"

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
