import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

engine = create_engine(
    DATABASE_URL.replace("postgres://", "postgresql://"),
    connect_args={"check_same_thread": False} if ENVIRONMENT == "dev" else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
