create table AWM.DIRECTION
(
    DIRECTION_ID NUMBER generated as identity
        primary key,
    NAME         VARCHAR2(2000) not null
)
/

create table AWM.SPECIALITY
(
    SPECIALITY_ID NUMBER generated as identity
        primary key,
    DIRECTION_ID  NUMBER         not null
        references AWM.DIRECTION,
    NAME          VARCHAR2(2000) not null,
    CODE          CHAR(8)        not null
)
/

create table AWM.UNIVERSITY
(
    UNIVERSITY_ID NUMBER generated as identity
        primary key,
    NAME          VARCHAR2(2000) not null
)
/

create table AWM.MEGA_FACULTY
(
    MEGA_FACULTY_ID NUMBER generated as identity
        primary key,
    UNIVERSITY_ID   NUMBER         not null
        references AWM.UNIVERSITY,
    NAME            VARCHAR2(2000) not null
)
/

create table AWM.FACULTY
(
    FACULTY_ID      NUMBER generated as identity
        primary key,
    MEGA_FACULTY_ID NUMBER         not null
        references AWM.MEGA_FACULTY,
    NAME            VARCHAR2(2000) not null
)
/

create table AWM.STUDY_GROUP
(
    STUDY_GROUP_ID NUMBER generated as identity
        primary key,
    FACULTY_ID     NUMBER   not null
        references AWM.FACULTY,
    SPECIALITY_ID  NUMBER   not null
        references AWM.SPECIALITY,
    CODE           CHAR(10) not null
)
/

create table AWM.PERSON
(
    PERSON_ID NUMBER generated as identity
        primary key,
    NAME      VARCHAR2(2000) not null
)
/

create table AWM.POSITION
(
    POSITION_ID NUMBER generated as identity
        primary key,
    NAME        VARCHAR2(2000) not null
)
/

create table AWM.STAFF
(
    STAFF_ID    NUMBER generated as identity
        primary key,
    PERSON_ID   NUMBER not null
        references AWM.PERSON,
    POSITION_ID NUMBER not null
        references AWM.POSITION
)
/

create table AWM.DEGREE
(
    DEGREE_ID NUMBER generated as identity
        primary key,
    NAME      VARCHAR2(2000) not null
)
/

create table AWM.EDUCATIONAL_FORM
(
    EDUCATIONAL_FORM_ID NUMBER generated as identity
        primary key,
    NAME                VARCHAR2(2000) not null
)
/

create table AWM.STUDENT
(
    STUDENT_ID    NUMBER generated as identity
        primary key,
    SPECIALITY_ID NUMBER not null
        references AWM.SPECIALITY,
    PERSON_ID     NUMBER not null
        references AWM.PERSON,
    DEGREE_ID     NUMBER not null
        references AWM.DEGREE
)
/

create table AWM.CLASSROOM
(
    CLASSROOM_ID NUMBER generated as identity
        primary key,
    POSITION     VARCHAR2(2000) not null
)
/

create table AWM.TIME_SLOT
(
    TIME_SLOT_ID NUMBER generated as identity
        primary key,
    NAME         VARCHAR2(2000) not null
)
/

create table AWM.DISCIPLINE
(
    DISCIPLINE_ID NUMBER generated as identity
        primary key,
    NAME          VARCHAR2(2000) not null
)
/

create table AWM.SPECIALITY_DISCIPLINE
(
    SPECIALITY_DISCIPLINE_ID NUMBER generated as identity
        primary key,
    SPECIALITY_ID            NUMBER not null
        references AWM.SPECIALITY,
    DISCIPLINE_ID            NUMBER not null
        references AWM.DISCIPLINE,
    PERSON_ID                NUMBER not null
        references AWM.PERSON,
    LECTURE_HOURS            NUMBER not null,
    LABORATORY_HOURS         NUMBER not null,
    PRACTICAL_HOURS          NUMBER not null,
    DATE_OF_SCORING          DATE   not null
)
/

create table AWM.STUDENT_GROUP
(
    STUDENT_GROUP_ID    NUMBER generated as identity
        primary key,
    STUDENT_ID          NUMBER    not null
        references AWM.STUDENT,
    STUDY_GROUP_ID      NUMBER    not null
        references AWM.STUDY_GROUP,
    EDUCATIONAL_FORM_ID NUMBER    not null
        references AWM.EDUCATIONAL_FORM,
    "from"              DATE      not null,
    "to"                DATE      not null,
    IS_PAID             NUMBER(1) not null,
    COURSE              NUMBER    not null
)
/

create table AWM.SCHEDULE
(
    SCHEDULE_ID              NUMBER generated as identity
        primary key,
    CLASSROOM_ID             NUMBER not null
        references AWM.CLASSROOM,
    SPECIALITY_DISCIPLINE_ID NUMBER not null
        references AWM.SPECIALITY_DISCIPLINE,
    STAFF_ID                 NUMBER not null
        references AWM.STAFF,
    TIME_SLOT_ID             NUMBER not null
        references AWM.TIME_SLOT,
    "date"                   DATE   not null
)
/

create table AWM.ACADEMIC_PERFORMANCE
(
    ACADEMIC_PERFORMANCE_ID  NUMBER generated as identity
        primary key,
    STUDENT_ID               NUMBER not null
        references AWM.STUDENT,
    SPECIALITY_DISCIPLINE_ID NUMBER not null
        references AWM.SPECIALITY_DISCIPLINE,
    SUBJECT_SCORE            NUMBER not null,
    ACADEMIC_SEMESTER        NUMBER not null
)
/

create table AWM.PROJECT
(
    PROJECT_ID NUMBER generated as identity
        primary key,
    NAME       VARCHAR2(2000) not null
)
/

create table AWM.BOOK
(
    BOOK_ID NUMBER generated as identity
        primary key,
    NAME    VARCHAR2(2000) not null
)
/

create table AWM.PUBLICATION_TYPE
(
    PUBLICATION_TYPE_ID NUMBER generated as identity
        primary key,
    NAME                VARCHAR2(2000) not null
)
/

create table AWM.EDITION_TYPE
(
    EDITION_TYPE_ID NUMBER generated as identity
        primary key,
    NAME            VARCHAR2(2000) not null
)
/

create table AWM.EDITION_PLACE
(
    EDITION_PLACE_ID NUMBER generated as identity
        primary key,
    NAME             VARCHAR2(2000) not null
)
/

create table AWM.EDITION_LANG
(
    EDITION_LANG_ID NUMBER generated as identity
        primary key,
    NAME            VARCHAR2(2000) not null,
    LOCALE          VARCHAR2(3)    not null
)
/

create table AWM.PROJECT_MEMBER
(
    PROJECT_MEMBER_ID NUMBER generated as identity
        primary key,
    PROJECT_ID        NUMBER not null
        references AWM.PROJECT,
    PERSON_ID         NUMBER not null
        references AWM.PERSON,
    START_DATE        DATE   not null,
    END_DATE          DATE   not null
)
/

create table AWM.CONFERENCE
(
    CONFERENCE_ID NUMBER generated as identity
        primary key,
    NAME          VARCHAR2(2000) not null,
    PLACE         VARCHAR2(2000) not null,
    START_DATE    DATE           not null
)
/

create table AWM.CONFERENCE_MEMBER
(
    CONFERENCE_MEMBER_ID NUMBER generated as identity
        primary key,
    CONFERENCE_ID        NUMBER not null
        references AWM.CONFERENCE,
    PERSON_ID            NUMBER not null
        references AWM.PERSON
)
/

create table AWM.EDITION
(
    EDITION_ID       NUMBER generated as identity
        primary key,
    NAME             VARCHAR2(2000) not null,
    VOLUME           NUMBER         not null,
    EDITION_PLACE_ID NUMBER         not null
        references AWM.EDITION_PLACE,
    EDITION_TYPE_ID  NUMBER         not null
        references AWM.EDITION_TYPE,
    EDITION_LANG_ID  NUMBER         not null
        references AWM.EDITION_LANG
)
/

create table AWM.PUBLICATION
(
    PUBLICATION_ID      NUMBER generated as identity
        primary key,
    NAME                VARCHAR2(2000) not null,
    PUBLICATION_TYPE_ID NUMBER         not null
        references AWM.PUBLICATION_TYPE,
    EDITION_ID          NUMBER         not null
        references AWM.EDITION,
    PERSON_ID           NUMBER         not null
        references AWM.PERSON,
    CITATION            NUMBER         not null,
    PUBLISHED_DATE      DATE           not null
)
/

create table AWM.PUBLICATION_COAUTHORS
(
    PUBLICATION_COAUTHORS_ID NUMBER generated as identity
        primary key,
    PUBLICATION_ID           NUMBER not null
        references AWM.PUBLICATION,
    PERSON_ID                NUMBER not null
        references AWM.PERSON
)
/

create table AWM.LIBRARY_CARD
(
    LIBRARY_CARD_ID NUMBER generated as identity
        primary key,
    PERSON_ID       NUMBER not null
        references AWM.PERSON,
    BOOK_ID         NUMBER not null
        references AWM.BOOK,
    TAKEN_DATE      DATE   not null,
    RETURNED_DATE   DATE   not null
)
/

create table AWM.HOSTEL
(
    HOSTEL_ID  NUMBER generated as identity
        primary key,
    LOCATION   VARCHAR2(2000) not null,
    ROOM_COUNT NUMBER         not null
)
/

create table AWM.ROOM
(
    ROOM_ID      NUMBER generated as identity
        primary key,
    "number"     NUMBER         not null,
    TYPE_ROOM    VARCHAR2(2000) not null,
    RESIDENTS    NUMBER         not null,
    DISINFECTION DATE           not null,
    BEDBUG       NUMBER(1)      not null,
    WARNING      NUMBER         not null
)
/

create table AWM.STUDENT_HOSTEL
(
    STUDENT_HOSTEL_ID NUMBER generated as identity
        primary key,
    STUDENT_ID        NUMBER         not null
        references AWM.STUDENT,
    "privileges"      NUMBER(1)      not null,
    TYPE_OF_TRAINING  VARCHAR2(2000) not null,
    PAYMENT           NUMBER         not null,
    VISIT             VARCHAR2(2000) not null,
    PERIOD_FROM       DATE           not null,
    PERIOD_TO         DATE           not null,
    ROOM_ID           NUMBER         not null
        references AWM.ROOM,
    HOSTEL_ID         NUMBER         not null
        references AWM.HOSTEL
)
/


