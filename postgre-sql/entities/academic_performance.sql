-- Table: university.academic_performance

-- DROP TABLE university.academic_performance;

CREATE TABLE university.academic_performance
(
    academic_performance_id bigint NOT NULL DEFAULT nextval('university.academic_performance_academic_performance_id_seq'::regclass),
    student_fid bigint NOT NULL,
    specialty_discipline_fid bigint NOT NULL,
    subject_score smallint NOT NULL,
    academic_semester smallint NOT NULL,
    CONSTRAINT academic_performance_pkey PRIMARY KEY (academic_performance_id),
    CONSTRAINT academic_performance_student_fid_specialty_discipline_fid_s_key UNIQUE (student_fid, specialty_discipline_fid, subject_score, academic_semester),
    CONSTRAINT specialty_discipline_id_too_academic_performance FOREIGN KEY (specialty_discipline_fid)
        REFERENCES university.specialty_discipline (specialty_discipline_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT student_id_too_academic_performance FOREIGN KEY (student_fid)
        REFERENCES university.student (student_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE university.academic_performance
    OWNER to postgres;