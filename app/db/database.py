
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

#configures database connectivity
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

#Creates session to interact with database (for operations like insertion, deletion)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False
)

#Parent class for our db models
class Base(DeclarativeBase):
    pass

#Provides session and closes it afterward
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
