import psycopg2

from config import settings


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            user=settings.DB_USER,
            password=settings.DB_PASS,
            dbname=settings.DB_NAME,
        )

    def get_all_users(self):
        cur = self.conn.cursor()

        # Execute a query
        cur.execute("SELECT * FROM users")

        # Retrieve query results
        records = cur.fetchall()
        cur.close()

        return records

    def add_user(self, email: str):
        cur = self.conn.cursor()

        # Execute a query
        cur.execute("INSERT INTO users (email) VALUES (%s);", (email,))
        self.conn.commit()

    def get_all_expenses(self):
        pass
    