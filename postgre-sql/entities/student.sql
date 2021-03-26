-- Table: university.student

-- DROP TABLE university.student;

CREATE TABLE university.student
(
    student_id bigint NOT NULL DEFAULT nextval('university.student_student_id_seq'::regclass),
    person_fid bigint NOT NULL,
    specialty_fid bigint NOT NULL,
    CONSTRAINT student_pkey PRIMARY KEY (student_id),
    CONSTRAINT student_person_fid_specialty_fid_key UNIQUE (person_fid, specialty_fid),
    CONSTRAINT person_id_too_student FOREIGN KEY (person_fid)
        REFERENCES university.person (person_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT specialty_id_too_student FOREIGN KEY (specialty_fid)
        REFERENCES university.specialty (specialty_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE university.student
    OWNER to postgres;