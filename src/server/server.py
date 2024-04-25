# Imports
from flask import Flask
from platform import system
from secrets import token_hex

from engine import engine
from models import Base
from session import session

# Setup database
Base.metadata.create_all(bind = engine)

# Initialize Flask
app = Flask(__name__)
app.secret_key = token_hex()

if system() == "Windows" and __name__ == "__main__":
	app.run()
