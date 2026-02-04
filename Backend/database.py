from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Use a local SQLite database for development and testing.
# If you want to use MySQL in production, replace this URL accordingly.
DATABASE_URL = "sqlite:///./hrms.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)