# pip install mysql-connector-python
import mysql.connector

db = mysql.connector.connect(
            host="itmo.fatalist.tech",
            user="root",
            password="P@ssw0rd"
        )
repository = "?"

print(db)
# TODO logic
db.close()
