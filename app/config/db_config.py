from config.path_config import DB_PATH
from sqlite3 import Connection, Cursor
import sqlite3
import os


def get_db_name() -> str:
    return os.environ.get('DB_NAME', 'example')


def get_db_conn() -> Connection:
    path = f"{DB_PATH}/{get_db_name()}.sql"
    return sqlite3.connect(path)


def get_db_cursor(conn: Connection) -> Cursor:
    return conn.cursor()
