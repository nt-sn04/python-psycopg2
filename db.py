import psycopg2

from config import settings

# Connect to your postgres DB
conn = psycopg2.connect(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    user=settings.DB_USER,
    password=settings.DB_PASS,
    dbname=settings.DB_NAME,
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM users")

# Retrieve query results
records = cur.fetchall()
for record in records:
    print(record)
