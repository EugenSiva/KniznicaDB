import psycopg2

conn = psycopg2.connect(
    database="br6qvfninpigled6pl5b",
    user="uo3tx8pzmxr19zx0ps1c",
    password="swTcR4le9TBLBvA2BkK1eS1l8BZ6sF",
    host="br6qvfninpigled6pl5b-postgresql.services.clever-cloud.com",
    port="50013")

cursor = conn.cursor()

cursor.execute('SELECT * FROM authors')
autori = cursor.fetchall()


cursor.execute('SELECT * FROM authors')
autor = cursor.fetchone()

cursor.close()
conn.close()