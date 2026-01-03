import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

# 1. Define Base FIRST so other files can import it without errors
Base = declarative_base()

# --- Secure Secret Retrieval ---
db_user = st.secrets["DB_USER"]
db_password = st.secrets["DB_PASSWORD"]
db_host = st.secrets["DB_HOST"]
db_port = int(st.secrets["DB_PORT"])
db_name = st.secrets["DB_NAME"]

# Build the connection parameters safely
connection_url = URL.create(
    drivername="postgresql",
    username=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name,
)

# --- Engine Configuration ---
engine = create_engine(
    connection_url,
    poolclass=NullPool,
    connect_args={'sslmode': 'require'}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()