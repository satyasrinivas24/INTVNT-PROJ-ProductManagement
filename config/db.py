import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

# Load environment variables from .env file
load_dotenv()

meta = MetaData()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

try:
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)

    # Connect to database
    with engine.connect() as conn:
        # Test connection with a simple query
        result = conn.execute(text("SELECT VERSION()"))
        db_version = result.fetchone()
        print("✅ Successfully connected to MySQL database")
        print(f"Database version: {db_version[0]}")

except SQLAlchemyError as e:
    print(f"❌ Error connecting to MySQL: {e}")