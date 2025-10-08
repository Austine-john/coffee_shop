import sqlite3

connection = sqlite3.connect('magazine.db')

cursor = connection.cursor()

cursor.execute(''' DROP TABLE IF EXISTS articles ''')

def create_tables():
    # Ensure foreign keys enforced
    cursor.execute("PRAGMA foreign_keys = ON;")
    # Create authors
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """)
    # Create magazines
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT
    );
    """)
    # Create articles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE,
        FOREIGN KEY (magazine_id) REFERENCES magazines(id) ON DELETE CASCADE
    );
    """)
    connection.commit()
    connection.close()
