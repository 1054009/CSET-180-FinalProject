from engine import engine
from sqlalchemy.orm import Session

database_session = Session(bind = engine)
