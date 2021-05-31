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


def handle_discipline():
    print("handle table 'discipline'")
    cursor_oracle.execute("SELECT * FROM \"laba\".discipline")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.discipline(discipline_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.discipline where (discipline_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_educational_form():
    print("handle table 'educational_form'")
    cursor_oracle.execute("SELECT * FROM \"laba\".educational_form")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.educational_form(educational_form_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.educational_form where (educational_form_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_faculty():
    print("handle table 'faculty'")
    cursor_oracle.execute("SELECT * FROM \"laba\".faculty")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['mega_id'], row['name']))
        sql = 'INSERT INTO awm.faculty(faculty_id, mega_faculty_id, name) SELECT :1,:2,:3 FROM dual where not exists(select * from awm.faculty where (faculty_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_mega_faculty():
    print("handle table 'mega_faculty'")
    cursor_oracle.execute("SELECT * FROM \"laba\".mega_faculty")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.mega_faculty(mega_faculty_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.mega_faculty where (mega_faculty_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_person():
    print("handle table 'person'")
    cursor_oracle.execute("SELECT * FROM \"laba\".person")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['last_name'] + " " + row['first_name'] + " " + row['middle_name']))
        sql = 'INSERT INTO awm.person(person_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.person where (person_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_position():
    print("handle table 'position'")
    cursor_oracle.execute("SELECT * FROM \"laba\".position")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['name']))
        sql = 'INSERT INTO awm.position(position_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.position where (position_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_schedule():
    print("handle table 'schedule'")
    cursor_oracle.execute("SELECT * FROM \"laba\".schedule")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['classroom_id'], row['discipline_id'], row['teacher_id'], row['time_slot_id'], row['date']))
        sql = 'INSERT INTO awm.schedule(schedule_id, classroom_id, speciality_discipline_id, staff_id, time_slot_id, date) SELECT :1,:2,:3,:4,:5,:6 FROM dual where not exists(select * from awm.schedule where (schedule_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_speciality():
    print("handle table 'speciality'")
    cursor_oracle.execute("SELECT * FROM \"laba\".speciality")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['direction_id'], row['code'], row['name']))
        sql = 'INSERT INTO awm.speciality(speciality_id, direction_id, name, code) SELECT :1,:2,:3,:4 FROM dual where not exists(select * from awm.speciality where (speciality_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_staff():
    print("handle table 'staff'")
    cursor_oracle.execute("SELECT * FROM \"laba\".staff")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['person_id'], row['position_id']))
        sql = 'INSERT INTO awm.staff(staff_id, person_id, position_id) SELECT :1,:2,:3 FROM dual where not exists(select * from awm.staff where (staff_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_student():
    print("handle table 'student'")
    cursor_oracle.execute("SELECT * FROM \"laba\".student")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            sql = 'SELECT * FROM \"laba\".student_group WHERE student_id=:id'
            student_group = cursor_oracle.execute(sql, [row['id']]).fetchone()
            if student_group is None:
                continue
            sql = 'SELECT * FROM \"laba\".study_group WHERE id=:id'
            study_group = cursor_oracle.execute(sql, [student_group['group_id']]).fetchone()
            if study_group is None:
                continue
            ins_items.append((row['id'], study_group['speciality_id'], row['person_id'], row['degree_id']))
        sql = 'INSERT INTO awm.student(student_id, speciality_id, person_id, degree_id) SELECT :1,:2,:3,:4 FROM dual where not exists(select * from awm.student where (student_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_student_group():
    print("handle table 'student_group'")
    cursor_oracle.execute("SELECT * FROM \"laba\".student_group")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['student_id'], row['group_id'], row['educational_form_id'], row['from'], row['to'], row['is_paid'], row['course']))
        sql = 'INSERT INTO awm.student_group(student_id, study_group_id, educational_form_id, from, to, is_paid, course) SELECT :1,:2,:3,:4,:5,:6,:7 FROM dual where not exists(select * from awm.student_group where (student_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_study_group():
    print("handle table 'study_group'")
    cursor_oracle.execute("SELECT * FROM \"laba\".study_group")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['faculty_id'], row['speciality_id'], row['code']))
        sql = 'INSERT INTO awm.study_group(study_group_id, faculty_id, speciality_id, code) SELECT :1,:2,:3,:4 FROM dual where not exists(select * from awm.study_group where (study_group_id = :1))'
        cursor_awm.executemany(sql, ins_items)
        db_awm.commit()
    print("done")


def handle_time_slot():
    print("handle table 'time_slot'")
    cursor_oracle.execute("SELECT * FROM \"laba\".time_slot")
    result = cursor_oracle.fetchall()

    batches = split_list(result, wanted_parts=len(result)//10000)
    for batch in batches:
        ins_items = []
        for row in batch:
            ins_items.append((row['id'], row['time']))
        sql = 'INSERT INTO awm.time_slot(time_slot_id, name) SELECT :1,:2 FROM dual where not exists(select * from awm.time_slot where (time_slot_id = :1))'
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
    handle_discipline()
    handle_educational_form()
    handle_faculty()
    handle_mega_faculty()
    handle_person()
    handle_position()
    handle_schedule()
    handle_speciality()
    handle_student()
    handle_student_group()
    handle_study_group()
    handle_time_slot()

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
