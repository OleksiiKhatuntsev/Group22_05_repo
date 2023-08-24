import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='group2005'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM addresses")
# print(cursor.fetchall())
print(cursor.fetchone())
b = 0
# print(a)
c = 0
