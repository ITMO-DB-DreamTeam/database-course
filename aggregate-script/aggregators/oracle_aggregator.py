import cx_Oracle
import time


def connect_to_oracle():
    cx_Oracle.init_oracle_client(lib_dir=r"../instantclient_19_10")
    dsn = cx_Oracle.makedsn("itmo.fatalist.tech", 1521, service_name="HIBD")
    result = cx_Oracle.connect(
        user="sys",
        password="P@ssw0rd",
        dsn=dsn,
        encoding="UTF-8",
        mode=cx_Oracle.SYSDBA,
    )
    print("Connected to Oracle DB.")
    return result


def connect_to_awm():
    # cx_Oracle.init_oracle_client(lib_dir=r"../instantclient_19_10")
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


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts)]


def handle_classroom():
    print("handle table 'classroom'")
    cursor_oracle.execute("SELECT * FROM \"laba\".classroom")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['position']))
        sql = 'INSERT INTO awm.classroom(classroom_id, position) SELECT :1,:2 FROM dual where not exists(select * from awm.classroom where (classroom_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_degree():
    print("handle table 'degree'")
    cursor_oracle.execute("SELECT * FROM \"laba\".degree")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.degree(degree_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.degree where (degree_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_direction():
    print("handle table 'direction'")
    cursor_oracle.execute("SELECT * FROM \"laba\".direction")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.direction(direction_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.direction where (direction_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")
cursor_awm, db_awm, cursor_oracle, db_oracle = None, None, None, None
try:
    start_time = time.time()
    db_oracle = connect_to_oracle()
    db_awm = connect_to_awm()

    cursor_oracle = db_oracle.cursor()
    cursor_awm = db_awm.cursor()

    handle_classroom()
    handle_degree()
    handle_direction()

    print("Время выполнения:", round(time.time() - start_time, 3), "сек.")
except Exception as e:
    print("ERROR ORACLE_AGGREGATOR:", e)
finally:
    if cursor_awm is not None:
        cursor_awm.close()
    if db_awm is not None:
        db_awm.close()
    print("Connection to Oracle AWM closed.")
    if cursor_oracle is not None:
        cursor_oracle.close()
    if db_oracle is not None:
        db_oracle.close()
    print("Connection to Oracle DB closed.")
