-- Table: university.teacher

-- DROP TABLE university.teacher;

CREATE TABLE university.teacher
(
    teacher_id bigint NOT NULL DEFAULT nextval('university.teacher_teacher_id_seq'::regclass),
    person_fid bigint,
    CONSTRAINT teacher_pkey PRIMARY KEY (teacher_id),
    CONSTRAINT person_id_too_teacher FOREIGN KEY (person_fid)
        REFERENCES university.person (person_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE university.teacher
    OWNER to postgres;