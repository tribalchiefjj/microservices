import psycopg2 # type: ignore
from .config import Config # type: ignore

def get_db_connection():
    return psycopg2.connect(Config.DATABASE_URL)
