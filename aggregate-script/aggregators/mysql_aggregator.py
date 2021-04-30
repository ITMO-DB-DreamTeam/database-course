# pip install mysql-connector-python
import mysql.connector

try:
    db = mysql.connector.connect(
                host="itmo.fatalist.tech",
                user="root",
                password="P@ssw0rd"
            )

    cursor = db.cursor()

    print("Connected to DB.", db)

    # persons
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
except Exception as e:
    print("ERROR MYSQL:", e)
