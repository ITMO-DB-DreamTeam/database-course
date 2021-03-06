create table person (
    id number generated by default as identity primary key,
    first_name varchar2(2000) not null,
    last_name varchar2(2000) not null,
    middle_name varchar2(2000) null,
    birth_date date not null,
    birth_place varchar2(2000) not null
);

create table direction (
    id number generated by default as identity primary key,
    name varchar2(2000) not null
);

create table degree (
    id number generated by default as identity primary key,
    name varchar2(100) not null
);

create table speciality (
    id number generated by default as identity primary key,
    direction_id number not null,
    code char(10) not null,
    name varchar(2000) not null,

    constraint fk_direction__id foreign key (direction_id) references direction (id)
);

create index idx_speciality__code on speciality (code);

create table mega_faculty (
    id number generated by default as identity primary key,
    name varchar2(2000) not null
);

create table faculty (
    id number generated by default as identity primary key,
    mega_id number not null,
    name varchar2(2000) not null,

    constraint fk_mega_faculty__id foreign key (mega_id) references mega_faculty (id)
);

create table study_group (
    id number generated by default as identity primary key,
    code char(10) not null,
    speciality_id number not null,
    faculty_id number not null,

    constraint fk_speciality__id foreign key (speciality_id) references speciality (id),
    constraint fk_faculty__id foreign key (faculty_id) references faculty (id)
);

create index idx_study_group__code on study_group (code);

create table student (
    id number generated by default as identity primary key,
    person_id number not null,
    degree_id number not null,

    constraint fk_person__id foreign key (person_id) references person (id),
    constraint fk_degree__id foreign key (degree_id) references degree (id)
);

create table educational_form (
    id number generated by default as identity primary key,
    name varchar2(2000)
);

create table student_group (
    student_id number not null,
    group_id number not null,
    is_paid number(1) not null,
    educational_form_id number(1),
    course number not null,
    "from" date not null,
    "to" date null,

    constraint pk_student_group primary key (student_id, group_id, "from"),
    constraint fk_study_group__id foreign key (group_id) references study_group (id),
    constraint fk_student__id foreign key (student_id) references student (id),
    constraint fk_educational_form__id foreign key (educational_form_id) references educational_form (id)
);

create index idx_student_group on student_group (group_id, student_id);

create table discipline (
    id number generated by default as identity primary key,
    name varchar2(2000)
);

create table position (
    id number generated by default as identity primary key,
    name varchar2(2000) not null
);

create table staff (
    id number generated by default as identity primary key,
    person_id number not null,
    position_id number not null,

    constraint fk_staff__person_id foreign key (person_id) references person (id),
    constraint fk_staff__position_id foreign key (position_id) references position (id)
);

create table time_slot (
    id number generated by default as identity primary key,
    time varchar2(100) not null
);

create table classroom (
    id number generated by default as identity primary key,
    position varchar2(200) not null
);

create table schedule (
    id number generated by default as identity primary key,
    discipline_id number not null,
    teacher_id number not null,
    "date" date not null,
    time_slot_id number not null,
    classroom_id number not null,

    constraint fk_schedule__discipline_id foreign key (discipline_id) references discipline (id),
    constraint fk_schedule__teacher_id foreign key (teacher_id) references staff (id),
    constraint fk_schedule__time_slot_id foreign key (time_slot_id) references time_slot (id),
    constraint fk_schedule__classroom_id foreign key (classroom_id) references classroom (id)
);