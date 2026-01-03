import os
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

# Build the connection parameters safely
# This avoids the "int(components['port'])" error entirely
connection_url = URL.create(
    drivername="postgresql",
    username="postgres.qavpzacavbxlsyaavhyy",
    password="_K6#5HtSi!%msUD", # Use your REAL password here, NO encoding!
    host="aws-1-eu-north-1.pooler.supabase.com",
    port=6543,
    database="postgres",
)

engine = create_engine(
    connection_url,
    poolclass=NullPool,
    connect_args={'sslmode': 'require'}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ... rest of your get_db() function

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()