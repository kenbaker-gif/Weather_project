import os
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

# 1. Try to get the URL from Streamlit Secrets, fallback to your config file
try:
    # This works on Streamlit Cloud
    DATABASE_URL = st.secrets["DATABASE_URL"]
except:
    # This works locally using your existing config.py
    from config import DATABASE_URL

# 2. Fix for special characters in passwords
# If the URL contains '@' in the password, SQLAlchemy can get confused about the 'port'
# We also ensure the prefix is 'postgresql://' for SQLAlchemy 2.0 compatibility
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Create engine with Supabase-specific settings
# poolclass=NullPool is REQUIRED for Supabase Transaction Mode (Port 6543)
engine = create_engine(
    DATABASE_URL, 
    echo=True,
    poolclass=NullPool,
    connect_args={'sslmode': 'require'}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()