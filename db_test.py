import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="portfolio_risk_db"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM portfolios")

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()