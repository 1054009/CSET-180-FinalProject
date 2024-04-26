# Imports
from platform import system

from app import app
from engine import engine
from models import Base
from session import session

# Setup database
Base.metadata.reflect(engine)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

if system() == "Windows" and __name__ == "__main__":
	app.run()
