import sqlite3
import os
from datetime import datetime, date
from contextlib import contextmanager

DATABASE = 'attendance_system.db'

def init_db():
    """Initialize the SQLite database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create student table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            section TEXT,
            status TEXT DEFAULT 'unregistered'
        )
    ''')
    
    # Create attendance table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id TEXT,
            name TEXT,
            section TEXT,
            time TEXT,
            date TEXT,
            FOREIGN KEY (id) REFERENCES student(id)
        )
    ''')
    
    # Create admin_signup table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_signup (
            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Create admin_login table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_login (
            admin_id INTEGER,
            username TEXT,
            login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (admin_id) REFERENCES admin_signup(admin_id)
        )
    ''')
    
    conn.commit()
    conn.close()

@contextmanager
def get_db():
    """Context manager for database connections."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def dict_from_row(row):
    """Convert sqlite3.Row to dictionary."""
    if row is None:
        return None
    return dict(row)
