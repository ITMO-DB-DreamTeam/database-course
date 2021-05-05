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


def handle_edition_place():
    print("handle table 'edition_place'")
    cursor_mysql.execute("SELECT * FROM laba.edition_place")
    result = cursor_mysql.fetchall()
    for i, row in enumerate(result):
        sql = 'SELECT * FROM awm.edition_place WHERE edition_place_id=:id'
        check = cursor_awm.execute(sql, [row['id']]).fetchone()
        if check is None:
            sql = 'INSERT INTO awm.edition_place(edition_place_id, name) VALUES(:id,:name)'
            cursor_awm.execute(sql, [row['id'], row['name']])
            db_awm.commit()
    print("done")


def handle_edition_lang():
    print("handle table 'edition_lang'")
    cursor_mysql.execute("SELECT * FROM laba.edition_lang")
    result = cursor_mysql.fetchall()
    for i, row in enumerate(result):
        sql = 'SELECT * FROM awm.edition_lang WHERE edition_lang_id=:id'
        check = cursor_awm.execute(sql, [row['id']]).fetchone()
        if check is None:
            sql = 'INSERT INTO awm.edition_lang(edition_lang_id, name, locale) VALUES(:id,:name,:locale)'
            cursor_awm.execute(sql, [row['id'], row['name'], row['locale']])
            db_awm.commit()
    print("done")


def handle_edition_type():
    print("handle table 'edition_type'")
    cursor_mysql.execute("SELECT * FROM laba.edition_type")
    result = cursor_mysql.fetchall()
    for i, row in enumerate(result):
        sql = 'SELECT * FROM awm.edition_type WHERE edition_type_id=:id'
        check = cursor_awm.execute(sql, [row['id']]).fetchone()
        if check is None:
            sql = 'INSERT INTO awm.edition_type(edition_type_id, name) VALUES(:id,:name)'
            cursor_awm.execute(sql, [row['id'], row['name']])
            db_awm.commit()
    print("done")


def handle_publication_type():
    print("handle table 'publication_type'")
    cursor_mysql.execute("SELECT * FROM laba.publication_type")
    result = cursor_mysql.fetchall()
    for i, row in enumerate(result):
        sql = 'SELECT * FROM awm.publication_type WHERE publication_type_id=:id'
        check = cursor_awm.execute(sql, [row['id']]).fetchone()
        if check is None:
            sql = 'INSERT INTO awm.publication_type(publication_type_id, name) VALUES(:id,:name)'
            cursor_awm.execute(sql, [row['id'], row['name']])
            db_awm.commit()
    print("done")


def handle_user_position():
    print("handle table 'position'")
    cursor_mysql.execute("SELECT * FROM laba.user_position")
    result = cursor_mysql.fetchall()
    for i, row in enumerate(result):
        sql = 'SELECT * FROM awm.position WHERE position_id=:id'
        check = cursor_awm.execute(sql, [row['id']]).fetchone()
        if check is None:
            sql = 'INSERT INTO awm.position(position_id, name) VALUES(:id,:name)'
            cursor_awm.execute(sql, [row['id'], row['name']])
            db_awm.commit()
    print("done")


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts)]


def handle_user():
    print("handle table 'user'")
    cursor_mysql.execute("SELECT * FROM laba.user")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_person = []
        ins_staff = []
        for row in batch:
            ins_person.append((row['id'], row['fio']))
            ins_staff.append((row['id'], row['position_id']))
        sql = 'INSERT INTO awm.person(person_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.person where (person_id = :1))'
        cursor_awm.executemany(sql, ins_person)
        sql = 'INSERT INTO awm.staff(person_id, position_id) SELECT :1,:2 FROM dual where not exists(select * from awm.staff where (person_id=:1 AND position_id=:2))'
        cursor_awm.executemany(sql, ins_staff)
        db_awm.commit()
    print("done")


def handle_book():
    print("handle table 'book'")
    cursor_mysql.execute("SELECT * FROM laba.book")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.book(book_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.book where (book_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_conference():
    print("handle table 'conference'")
    cursor_mysql.execute("SELECT * FROM laba.conference")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name'], row['place'], row['started']))
        sql = 'INSERT INTO awm.conference(conference_id, name, place, start_date) SELECT :1,:2,:3,:4 FROM dual where not exists(select * from awm.conference where (conference_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_conference_member():
    print("handle table 'conference_member'")
    cursor_mysql.execute("SELECT * FROM laba.conference_member")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['conference_id'], row['user_id']))
        sql = 'INSERT INTO awm.conference_member(conference_id, person_id) SELECT :1,:2 FROM dual where not exists(select * from awm.conference_member where (conference_id = :1 AND person_id = :2))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_edition():
    print("handle table 'edition'")
    cursor_mysql.execute("SELECT * FROM laba.edition")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name'], row['volume'], row['place_id'], row['type_id'], row['lang_id']))
        sql = 'INSERT INTO awm.edition(edition_id, name, volume, edition_place_id, edition_type_id, edition_lang_id) SELECT :1,:2,:3,:4,:5,:6 FROM dual where not exists(select * from awm.edition where (edition_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_library_card():
    print("handle table 'library_card'")
    cursor_mysql.execute("SELECT * FROM laba.library_card")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['user_id'], row['book_id'], row['tooked'], row['returned']))
        sql = 'INSERT INTO awm.library_card(person_id, book_id, taken_date, returned_date) SELECT :1,:2,:3,:4 FROM dual where not exists(select * from awm.library_card where (person_id = :1 AND book_id = :2 AND taken_date = :3 AND returned_date = :4))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_project():
    print("handle table 'project'")
    cursor_mysql.execute("SELECT * FROM laba.project")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.project(project_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.project where (project_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_project_member():
    print("handle table 'project_member'")
    cursor_mysql.execute("SELECT * FROM laba.project_member")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['project_id'], row['user_id'], row['started'], row['ended']))
        sql = 'INSERT INTO awm.project_member(project_id, person_id, start_date, end_date) SELECT :1,:2,:3,:4 FROM dual where not exists(select * from awm.project_member where (project_id = :1 AND person_id = :2 AND start_date = :3 AND end_date = :4))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_publication():
    print("handle table 'publication'")
    cursor_mysql.execute("SELECT * FROM laba.publication")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name'], row['type_id'], row['edition_id'], row['user_id'], row['citation'], row['published']))
        sql = 'INSERT INTO awm.publication(publication_id, name, publication_type_id, edition_id, person_id, citation, published_date) SELECT :1,:2,:3,:4,:5,:6,:7 FROM dual where not exists(select * from awm.publication where (publication_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_publication_co_authors():
    print("handle table 'publication_co-authors'")
    cursor_mysql.execute("SELECT * FROM laba.publication_co-authors")
    result = cursor_mysql.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['publication_id'], row['user_id']))
        sql = 'INSERT INTO awm.publication_coauthors(publication_id, person_id) SELECT :1,:2 FROM dual where not exists(select * from awm.publication_coauthors where (publication_id = :1 AND person_id = :2))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


cursor_awm, db_awm, cursor_mysql, db_mysql = None, None, None, None
# main script
try:
    db_mysql = connect_to_mysql()
    db_awm = connect_to_awm()

    cursor_mysql = db_mysql.cursor(dictionary=True)
    cursor_awm = db_awm.cursor()

    # handle_edition_place()
    # handle_edition_lang()
    # handle_edition_type()
    # handle_publication_type()
    # handle_user_position()
    # handle_user()
    # handle_book()
    # handle_conference()
    # handle_conference_member()
    handle_edition()
    handle_library_card()
    handle_project()
    handle_project_member()
    handle_publication()
    handle_publication_co_authors()

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
