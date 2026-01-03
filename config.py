import os
from dotenv import load_dotenv

load_dotenv()

# Weather API
API_KEY = os.getenv("API_KEY")

# PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")  # must exist in .env
DB_OPTIONS = os.getenv("DB_OPTIONS", "")  # should be ?sslmode=require

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    f"{DB_OPTIONS}"  # ONLY this, do NOT append API_KEY
)
