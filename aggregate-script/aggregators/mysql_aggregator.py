import mysql.connector
import cx_Oracle


def connect_to_mysql():
    result = mysql.connector.connect(
        host="itmo.fatalist.tech",
        user="root",
        password="P@ssw0rd"
    )
    print("Connected to MySQL.")
    return result


def connect_to_awm():
    cx_Oracle.init_oracle_client(lib_dir=r"../instantclient_19_10")
    dsn = cx_Oracle.makedsn("itmo.fatalist.tech", 1522, service_name="xe")
    result = cx_Oracle.connect(
        user="sys",
        password="oracle",
        dsn=dsn,
        encoding="UTF-8",
        mode=cx_Oracle.SYSDBA,
    )
    print("Connected to Oracle AWM.")
    return result


cursor_awm, db_awm, cursor_mysql, db_mysql = None, None, None, None
# main script
try:
    db_mysql = connect_to_mysql()
    db_awm = connect_to_awm()

    cursor_mysql = db_mysql.cursor()
    cursor_awm = db_awm.cursor()

    # persons
    cursor_mysql.execute("SELECT * FROM laba.user")
    result = cursor_mysql.fetchall()
    for row in result:
        print(row)


except Exception as e:
    print("ERROR MYSQL_AGGREGATOR:", e)
finally:
    if cursor_awm is not None:
        cursor_awm.close()
    if db_awm is not None:
        db_awm.close()
    print("Connection to Oracle AWM closed.")
    if cursor_mysql is not None:
        cursor_mysql.close()
    if db_mysql is not None:
        db_mysql.close()
    print("Connection to MySQL closed.")
