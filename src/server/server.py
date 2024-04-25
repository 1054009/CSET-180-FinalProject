# Imports
from platform import system

from app import app
from engine import engine
from models import Base
from session import session

# Setup database
Base.metadata.create_all(bind = engine)

if system() == "Windows" and __name__ == "__main__":
	app.run()
